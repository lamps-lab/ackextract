from xml.dom.minidom import parse
import re
import pysbd
from stanfordcorenlp import StanfordCoreNLP
import requests
from time import sleep

def grobid(pdfname):    #input PDFfilename output XMLfilename
    url = 'http://localhost:8070/api/processFulltextDocument'
    params=dict(input=open(pdfname,'rb'))
    tei = requests.post(url,files=params,timeout=300)
    teiname = r'%s.tei'%(pdfname)
    fh = open(teiname,'w',encoding='utf-8')
    fh.write(tei.text)
    fh.close()
    return teiname
# def pdf2txt(pdfname):

def grobidNer(pdfname):
    return ackNeExtract(grobid(pdfname))
def grobidPer(pdfname):
    return ackPerExtract(grobid(pdfname))
def grobidOrg(pdfname):
    return ackOrgExtract(grobid(pdfname))
def grobidPerPure(pdfname):
    return ackPerExtractPure(grobid(pdfname))
def grobidOrgPure(pdfname):
    return ackOrgExtractPure(grobid(pdfname))
def grobidAuthor(pdfname):
    return authorName(grobid(pdfname))



def ackNeExtract(pfname):
      
    return ackPerExtract(pfname),ackOrgExtract(pfname)
    
      
def ackPerExtract(pfname):
    a = perNER(XML2ack(pfname))
    b = authorName(pfname)
    return [item for item in a if item[0] not in b]


def ackOrgExtract(pfname):
    
    return orgNER(XML2ack(pfname))
    

def ackPerExtractPure(pfname):
    a = perNERString(XML2ack(pfname))
    b = authorName(pfname)
    return [item for item in a if item not in b]


def ackOrgExtractPure(pfname):
    
    return orgNERString(XML2ack(pfname))


def txtPerExtractPure(txt):
    return perNERString(tokenize(txt))

def txtOrgExtractPure(txt):
    return orgNERString(tokenize(txt))

def authorName(pfname):
    def allChildren(node):
        content = ''
        nodelist = node.childNodes
        for node in nodelist:
            if node.nodeType != node.TEXT_NODE:
                content = content + allChildren(node)
            else:
                nodedata = node.data
                content = content + nodedata
        return content
    
    authorname=[]
    
    doc = parse(pfname)
    header = doc.getElementsByTagName('teiHeader')
    for h in header:
        author = h.getElementsByTagName('author')
        for a in author:
            persrname=a.getElementsByTagName('persName')
            for n in persrname:
                name0 = allChildren(n)
                name1 = re.findall('[A-Z][^A-Z]*',name0)
                name2 = ''
                for m in name1:
                    name2+=m
                    name2+=' '
                authorname.append(name2.strip())
    
    authorname = list(dict.fromkeys(authorname))
    return(authorname)
    

def XML2ack(pfname):
    pattern1 = re.compile('acknowledg|funding|beneﬁt', re.IGNORECASE)
    pattern2 = re.compile('thank[s]? |grateful|gratitude|funded', re.IGNORECASE) #not recommend 'fund','acknowledgement'and'benifit'
    temp_list = []
    text = ''
    textout = ''
    
    
    def allChildren(node):
        content = ''
        nodelist = node.childNodes
        for node in nodelist:
            if node.nodeType != node.TEXT_NODE:
                content = content + allChildren(node)
            else:
                nodedata = node.data
                content = content + nodedata
        return content
    
    
    try:
        doc = parse(pfname)
        divs = doc.getElementsByTagName('div')
        hasacknowledgement = 0
        for div in divs:
            divtype = div.getAttribute("type")
            if divtype == 'acknowledgement' or divtype == 'annex':
                div2s = div.getElementsByTagName('div')
                for div2 in div2s:
                    heads = div2.getElementsByTagName('head')
                    hashead = 0
                    for head in heads:
                        hashead = 1
                        ack = allChildren(head)
                        if pattern1.search(ack):
                            #print (ack+',')     #part title
                            text = text + ack+',' 
                            
                            ps = div2.getElementsByTagName('p')
                            for p in ps:
                                hasacknowledgement = 1
                                pdata = allChildren(p)
                                #print(pdata)
                                text = text + pdata+'\n'
                                temp_list.append(pdata)
                                
                    if hashead == 0:
                        p0s = div2.getElementsByTagName('p')
                        for p0 in p0s:
                            p0data = allChildren(p0)
                            if pattern1.search(p0data):
                                hasacknowledgement = 1
                                #print(p0data)
                                text = text + p0data + '\n'
                                temp_list.append(p0data)
                                
                                
        #if hasacknowledgement == 0:
        divs = doc.getElementsByTagName('div')
        for div in divs:
            ps = div.getElementsByTagName('p')
            for p in ps:
                pdata = allChildren(p)
                if pattern2.search(pdata):
                    saved = 0
                    for savedstr in temp_list:
                        if pdata == savedstr:
                            saved = 1
                            break
                    if saved == 0:
                        #print(pdata)
                        textout = textout + pdata + '\n'
                        temp_list.append(pdata)
                        
                        
        notes = doc.getElementsByTagName('note')
        for note in notes:
            notedata = allChildren(note)
            if pattern2.search(notedata):
                #print(notedata)
                textout = textout + notedata + '\n'
        
        figures = doc.getElementsByTagName('figure')
        for figure in figures:
            figuredata = allChildren(figure)
            if pattern2.search(figuredata):
                #print(notedata)
                textout = textout + figuredata + '\n'
        
    except Exception as e:
        print('')
    
    
    
    
    text = filter1(tokenize(text))
    textout = filter1(tokenize(textout))
    #print(text,textout)
    textsum = text+textout
   
    return textsum



def tokenize(text):
    seg = pysbd.Segmenter(language="en", clean=False)
    return seg.segment(text)


def perNER(sentencelist):
    nlp = StanfordCoreNLP('http://localhost', port=9000, timeout=30000)
    PER=[]
    Pres=[]
    for t in sentencelist:
        ner = nlp.ner(t)
  
        p=''
        for n in ner:
            if n[1]=='PERSON':
                p = p + n[0] + ' '
            if n[1]!='PERSON':
                if p != '':
                    PER.append((p.strip(),'PER'))                
                    p = ''       
    
    nlp.close()
    PER = list(dict.fromkeys(PER))
    for p in PER:  # names to be acknowledged must be full name
        if p[0].find(' ')!= -1 or p[0].find('.')!=-1:
            Pres.append(p)
    
    return Pres
    
def orgNER(sentencelist):
    nlp = StanfordCoreNLP('http://localhost', port=9000, timeout=30000)
    ORG=[]
          
    for t in sentencelist:
        ner = nlp.ner(t)
        o=''            
        for n in ner:
            if n[1]=='ORGANIZATION':
                o = o + n[0] + ' '
            if n[1]!='ORGANIZATION':
                if o != '':
                    ORG.append((o.strip(),'ORG'))
                    
                    o = ''
    nlp.close()
    ORG = list(dict.fromkeys(ORG))
    return ORG    

def perCounter(list1,list2):
    m=0
    for a in list1:
        a = a.rstrip()
        for b in list2:
            b = b.rstrip()
            if a == b:
                print(a,'&&&',b)
                m+=1
    try:
        recall = m/len(list1)
        print('recall = ', recall*100,'%')
    except:
        recall = None
       
    try:
        precision = m/len(list2)
        print('precision = ', precision*100,'%')
    except:
        precision = None
    
    try:
        F1 = (2*recall*precision)/(recall+precision)
        print("F1 =",F1)
    except:
        F1 = None
    
    return recall, precision, F1, m,len(list1),len(list2)
    

def orgCounter_strict(list1,list2):
    
    

    # strict evaluation
    m = 0
    n = 0
    for a in list1:
        t = False
        a = a.rstrip()
        for b in list2:
            b = b.rstrip()
            if a == b:
                print('recall: \n',a,'&&&',b)
                
                t = True
        if t == True:
            n+=1
    
    for b in list2:
        t = False
        b = b.rstrip()
        for a in list1:
            a = a.rstrip()
            if a == b:
                print('precision: \n',b,'&&&',a)
                
                t = True
        if t == True:
            m+=1
    try:
        recall0 = n/len(list1)
        print('recall = ', recall0*100,'%')
    except:
        recall0 = None
       
    try:
        precision0 = m/len(list2)   #strict
        print('precision = ', precision0*100,'%')
    except:
        precision0 = None
    
    try:
        F10 = (2*recall0*precision0)/(recall0+precision0)
        print("F1 =",F10)
    except:
        F10 = None        
    return recall0, precision0, F10, m, len(list1), len(list2),n

# return can be optimised
def orgCounter_loose(list1,list2):
    
    
    # loose evaluation
    m=0
    n=0
    for a in list1:
        t = False
        a = a.rstrip()
        for b in list2:
            b = b.rstrip()
            if a.find(b)!=-1 or b.find(a)!=-1:
                print('recall:  \n',a,'&&&',b)
                t = True
                
        if t == True:
            m+=1
    
    for b in list2:
        t = False
        b = b.rstrip()
        
        for a in list1:
            a = a.rstrip()
            if a.find(b)!=-1 or b.find(a)!=-1:
                print('recall:  \n',a,'&&&',b)
                t = True
                
        if t == True:
            n+=1

    try:
        recall0 = m/len(list1)
        print('recall = ', recall0*100,'%')
    except:
        recall0 = None
       
    try:
        precision0 = n/len(list2) #loose
        print('precision = ', precision0*100,'%')
    except:
        precision0 = None
    
    try:
        F10 = (2*recall0*precision0)/(recall0+precision0)
        print("F1 =",F10)
    except:
        F10 = None        
    return recall0, precision0, F10, m, len(list1), len(list2),n


def perNERString(sentencelist):
    nlp = StanfordCoreNLP('http://localhost', port=9000, timeout=30000)
    PER=[]
    Pres=[]
    for t in sentencelist:
        ner = nlp.ner(t)
  
        p=''
        for n in ner:
            if n[1]=='PERSON':
                p = p + n[0] + ' '
            if n[1]!='PERSON':
                if p != '':
                    PER.append(p.strip())                
                    p = ''       
    
    nlp.close()
    PER = list(dict.fromkeys(PER))
    for p in PER:
        if p.find(' ') != -1 or p.find('.') != -1:
            Pres.append(p)
    # print(Pres)
    return Pres
    
def orgNERString(sentencelist):
    nlp = StanfordCoreNLP('http://localhost', port=9000, timeout=30000)
    ORG=[]
          
    for t in sentencelist:
        ner = nlp.ner(t)
        o=''            
        for n in ner:
            if n[1]=='ORGANIZATION':
                o = o + n[0] + ' '
            if n[1]!='ORGANIZATION':
                if o != '':
                    ORG.append(o.strip())
                    
                    o = ''
    nlp.close()
    ORG = list(dict.fromkeys(ORG))
    return ORG    


def filter1(a):
    pattern3 = re.compile('thank|grateful|gratitude|fund|acknowledg|indebted|helpful|support|benefit|approved|dedicated|useful|provided|assistance|served as editor|served as associate editor|served as co-editor ', re.IGNORECASE)    #feedback provided strengthened 
    text2 =[]
    for r in a:   
        if pattern3.search(r):
            text2.append(r)
    return text2
    

    

