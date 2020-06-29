import json
import re
import pysbd
from stanfordcorenlp import StanfordCoreNLP
import requests
from time import sleep





def ackNeExtract(pfname):
      
    return ackPerExtract(pfname),ackOrgExtract(pfname)
    
      
def ackPerExtract(pfname):
    a = perNER(ackextract(pfname))
    b = authorName2(pfname)
    return [item for item in a if item[0] not in b]


def ackOrgExtract(pfname):
    
    return orgNER(ackextract(pfname))
    

def ackPerExtractPure(pfname):
    a = perNERString(ackextract(pfname))
    b = authorName2(pfname)
    return [item for item in a if item not in b]


def ackOrgExtractPure(pfname):
    
    return orgNERString(ackextract(pfname))


def txtPerExtractPure(txt):
    return perNERString(tokenize(txt))

def txtOrgExtractPure(txt):
    return orgNERString(tokenize(txt))

def authorName2(pfname):
    
    
    authorname=[]
    
    with open(pfname) as f:
        data =json.load(f)
        
        for x,y in data.items():
            if x == "metadata":
                for m in y['authors']:     
                    try:
                        # print(m)
                        name=''
                        name2=''
                        name3=''
                        name4=''
                        name5=''
                        name6=''
                        name7=''
                        name8=''
                        if len(m["middle"]) != 0:
                            name = m["first"].strip(' ;,')+' '+m["middle"][0].strip(' ;,')+' '+m["last"].strip(' ;,')
                            name2 =m["first"].strip(' ;,')[0]+' '+m["last"].strip(' ;,')
                            name3 =m["first"].strip(' ;,')[0]+'. '+m["last"].strip(' ;,')
                            name5 =m["first"].strip(' ;,')[0]+'.'+m["last"].strip(' ;,')
                            
                            name4 = m["first"].strip(' ;,')[0]+'. '+m["middle"][0].strip(' ;,')[0]+'. '+m["last"].strip(' ;,')
                            name6 = m["first"].strip(' ;,')[0]+'.'+m["middle"][0].strip(' ;,')[0]+'. '+m["last"].strip(' ;,')
                        else:
                            name = m["first"].strip(' ;,')+' '+m["last"].strip(' ;,')
                            name7 = m["first"].strip(' ;,')[0]+'. '+m["last"].strip(' ;,')       
                            name8 = m["first"].strip(' ;,')[0]+'.'+m["last"].strip(' ;,')  
                        
                        authorname.append(name.strip())
                        authorname.append(name2.strip())
                        authorname.append(name3.strip())
                        authorname.append(name4.strip())
                        authorname.append(name5.strip())
                        authorname.append(name6.strip())
                        authorname.append(name7.strip())
                        authorname.append(name8.strip())
                    except:
                        pass
    authorname = list(dict.fromkeys(authorname))
    return authorname

def authorName(pfname):
    
    
    authorname=[]
    
    with open(pfname) as f:
        data =json.load(f)
        
        for x,y in data.items():
            if x == "metadata":
                for m in y['authors']:     
                    print(m)
                    name=''
                    if len(m["middle"]) != 0:
                        name = m["first"].strip(' ;,')+' '+m["middle"][0].strip(' ;,')+' '+m["last"].strip(' ;,')
                        
                    else:
                        name = m["first"].strip(' ;,')+' '+m["last"].strip(' ;,')
                                         
                    authorname.append(name.strip())
                
    
    authorname = list(dict.fromkeys(authorname))
    return authorname

def ackextract(pfname):
    
    
    with open(pfname) as f:
        data =json.load(f)
        textlist=[]
        # pattern = re.compile('indebted', re.IGNORECASE) 
        pattern = re.compile('thank(?!s to)|grateful|gratitude|like[s]? to acknowledge|acknowledge[ds]? (.*?)(grant|contribution|constructive|scholarship|fellowship|Foundation|Institute|fund|financial)|indebted to|funded (by|in|through)|funding(:|support|came|assistance)|(supported by|with (the )?support of) (.*?)(grant|scholarship|fellowship|Foundation|Institute|fund|financial)|financially supported|(work|paper|study) was supported in part by|(helpful|useful) comments', re.IGNORECASE) 

        pattern2 = re.compile('acknowledgement|acknowledgment|funding', re.IGNORECASE) #section title
        for x,y in data.items():
            if x == 'body_text':
                
                for i in y:
                    if pattern.search(i['text']):
                        
                        
                        textlist+=filter1(tokenize(i['text']))
            if x == 'ref_entries':
                
                for i in y.values():
                    if pattern.search(i['text']):
                        textlist+=filter1(tokenize(i['text']))
            # if x == 'back_matter':          
                # for i in y:
                    # if pattern2.search(i['section']):
                        
                        # textlist+=tokenize(i['section']+',')
                        
                        # textlist+=tokenize(i['text'])
    
    
    
    
    
   
    return textlist



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
                    ORG.append(o.strip())
                    
                    o = ''
    nlp.close()
    ORG = list(dict.fromkeys(ORG))
    
    for x,i in enumerate(ORG):
        if 'Grant' == i[-1]:     
            ORG[x] = i.split('Grant')[0].strip()
        ORG[x] = (ORG[x],'ORG')
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
    

def orgCounter_strict(list1,list2): #list1:ground truth, list2:extraction
    
    

    # strict evaluation
    count_correct_ext = 0       #correct of extraction(list2)
    count_correct_GT = 0     #correct of ground truth(list1)
    for a in list1:         #recall
        t = False
        a = a.strip()
        for b in list2:
            b = b.strip()
            if a == b:
                # print(a,'&&&',b)   
                
                t = True
        if t == True:
            count_correct_GT+=1
    
    for b in list2:         #precision
        t = False
        b = b.strip()
        for a in list1:
            a = a.strip()
            if a == b:
                # print(b,'&&&',a)    
                
                t = True
        if t == True:
            count_correct_ext+=1
    try:
        recall0 = count_correct_GT/len(list1)
        print('recall = ', recall0*100,'%')
    except:
        recall0 = None
       
    try:
        precision0 = count_correct_ext/len(list2)   #strict
        print('precision = ', precision0*100,'%')
    except:
        precision0 = None
    
    try:
        F10 = (2*recall0*precision0)/(recall0+precision0)
        print("F1 =",F10)
    except:
        F10 = None        
    return recall0, precision0, F10, count_correct_GT, len(list1), count_correct_ext, len(list2)

# return can be optimised
def orgCounter_loose(list1,list2):
    
    
    # loose evaluation
    count_correct_GT=0
    count_correct_ext=0
    for a in list1:
        t = False
        a = a.strip()
        for b in list2:
            b = b.strip()
            if a.find(b)!=-1 or b.find(a)!=-1:
                # print(a,'&&&',b)
                t = True
                
        if t == True:
            count_correct_GT+=1
    
    for b in list2:
        t = False
        b = b.strip()
        
        for a in list1:
            a = a.strip()
            if a.find(b)!=-1 or b.find(a)!=-1:
                # print(a,'&&&',b)
                t = True
                
        if t == True:
            count_correct_ext+=1

    try:
        recall0 = count_correct_GT/len(list1)
        print('recall = ', recall0*100,'%')
    except:
        recall0 = None
       
    try:
        precision0 = count_correct_ext/len(list2) #loose
        print('precision = ', precision0*100,'%')
    except:
        precision0 = None
    
    try:
        F10 = (2*recall0*precision0)/(recall0+precision0)
        print("F1 =",F10)
    except:
        F10 = None        
    return recall0, precision0, F10, count_correct_GT, len(list1),count_correct_ext, len(list2)


def perNERString(sentencelist):
    PER = []
    for i in perNER(sentencelist):
        PER.append(i[0])
    
    
    
    return PER
    
def orgNERString(sentencelist):
    ORG = []
    for i in orgNER(sentencelist):
        ORG.append(i[0])
    
    
    
    return ORG  


def filter1(a):
    pattern3 = re.compile('thank|grateful|gratitude|fund|acknowledg|indebted|helpful|support|benefit|approved|dedicated|useful|provided|assistance', re.IGNORECASE)    #feedback provided strengthened 
    text2 =[]
    for r in a:   
        if pattern3.search(r):
            text2.append(r)
    return text2
    

    

