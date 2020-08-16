# this version test without Grobid
from stanza import *
# from NLTKNER import *
# from stanfordnlp import *
from spacyNER import *
import os


bingoP = 0
GTP = 0
FDP = 0

bingoOL = 0
bingoOLp = 0
GTOL = 0
FDOL = 0

bingoOS = 0
bingoOSp = 0
GTOS = 0
FDOS = 0


for i in os.listdir() :
    
    
    Person = []
    Org = []
    hasann = False
    
    
    if i.endswith('.ann'):              # find .ann file and collecting ground truth
        print(i)
            
        fileann = open(i,'r',encoding='utf-8')
        textann = fileann.readlines()
            
        for t in textann:
            # print('t: ',t)
            a = t.split('\t')
            # print("a: ")
            if 'Person' in a[1] or 'PER' in a[1]:
                Person.append(a[2].rstrip())
                
            
            if 'Organization' in a[1] or 'ORG' in a[1]:
                s = a[2].rstrip()
                if s[:3]=='the':
                    s=s[4:]
                Org.append(s)
    
        Person = list(dict.fromkeys(Person))            #Person ground truth
        Org = list(dict.fromkeys(Org))                  #Org ground truth
        # print(Person,Org)
    
        for x in os.listdir() :
            if x == i.split('.')[0]+'.txt':
                print(x)
                filei = open(x,'r',encoding='utf-8')
                texti = filei.read()
                # texti = tokenize(text)
                
                result = perCounter(Person,NERper(texti))  #NLTK spacy
                # result = perCounter(Person,perNERString(texti))
                print(Person)
                # print(perNERString(texti))
                print(result)
                bingoP+=result[3]
                GTP+=result[4]
                FDP+=result[5]
                
                resultOrgLoose = orgCounter_loose(Org,NERorg(texti))  #NLTK spacy
                # resultOrgLoose = orgCounter_loose(Org,orgNERString(texti))
                print(Org)
                # print(orgNERString(texti))
                print(resultOrgLoose)
                
                bingoOL += resultOrgLoose[3]
                bingoOLp += resultOrgLoose[5]
                GTOL += resultOrgLoose[4]
                FDOL += resultOrgLoose[6]
                
                resultOrgStrict = orgCounter_strict(Org,NERorg(texti))  #NLTK spacy
                # resultOrgStrict = orgCounter_strict(Org,orgNERString(texti))
                # print(resultOrgStrict)
                bingoOS += resultOrgStrict[3]
                bingoOSp += resultOrgStrict[5]
                GTOS += resultOrgStrict[4]
                FDOS += resultOrgStrict[6]
        
    
    
print(bingoP,GTP,FDP)
print(bingoOL,GTOL,bingoOLp,FDOL)
print(bingoOS,GTOS,bingoOSp,FDOS)

recallPerson = bingoP/GTP
precisionPerson = bingoP/FDP
F1Person = (2*recallPerson*precisionPerson)/(recallPerson+precisionPerson)
print('Person recall = ', recallPerson, 'Person precision = ', precisionPerson, 'Person F1 = ', F1Person)

recallOrgL = bingoOL/GTOL
precisionOrgL = bingoOLp/FDOL
F1OrgL = (2*recallOrgL*precisionOrgL)/(recallOrgL+precisionOrgL)
print('Orgloose recall = ', recallOrgL, 'Orgloose precision = ', precisionOrgL, 'Orgloose F1 = ',F1OrgL)

recallOrgS = bingoOS/GTOS
precisionOrgS = bingoOSp/FDOS
F1OrgS = (2*recallOrgS*precisionOrgS)/(recallOrgS+precisionOrgS)
print('Orgstrict recall = ', recallOrgS, 'Orgstrict precision = ', precisionOrgS, 'Orgstrict F1 = ',F1OrgS)    
