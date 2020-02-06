from xml.dom.minidom import parse
import re

pattern1 = re.compile('acknowledg|funding', re.IGNORECASE)
pattern2 = re.compile('thank[s]? |grateful|gratitude|funding', re.IGNORECASE)

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

print('Start:')

pfname = 'Evans_BritJournPoliSci_2012_d1Zm.pdf.tei'
temp_list = []
text = ''
textout = ''

    
n = 1

if 1==1:
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
                
        
        
    except Exception as e:
        print('XML document has error!')
        
        #print(e.message)
    #print('---------------------------------------------------\n')
    

print('text: ', text)
print('textout: ',textout)

import pysbd
seg = pysbd.Segmenter(language="en", clean=False)   
text = seg.segment(text)
textout = seg.segment(textout)
print (text)
print (textout)


text2 =[]

pattern3 = re.compile('thank[s]? |grateful|gratitude|fund|acknowledg|indebted|helpful|support', re.IGNORECASE)
for r in textout:   
    if pattern3.search(r):
        text2.append(r)

print (text2)


text2 = text + text2


from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP(r'C:\PWang\Datasets\NER\stanford\stanford_NLP')
PER=[]
ORG=[]


for t in text2:
    ner = nlp.ner(t)
    print(ner)


    p=''
    for n in ner:
        if n[1]=='PERSON':
            p = p + n[0] + ' '
        if n[1]!='PERSON':
            if p != '':
                PER.append((p,'PER'))                
                p = ''
    o=''            
    for n in ner:
        if n[1]=='ORGANIZATION':
            o = o + n[0] + ' '
        if n[1]!='ORGANIZATION':
            if o != '':
                ORG.append((o,'ORG'))
                
                o = ''
nlp.close()
print(PER)
print(ORG)


                
