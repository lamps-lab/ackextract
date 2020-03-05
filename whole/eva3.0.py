from ackseer import *
import os
import glob

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


for f in [x[0] for x in os.walk(r'C:\PWang\Datasets\2ndGT')][1:]:
    os.chdir(f)
    
    Person = []
    Org = []
    hasann = False
    try:
        for i in os.listdir(os.getcwd()):
            if i.endswith('.ann'):
                print(i)
                hasann = True
                fileann = open(i,'r',encoding='utf-8')
                textann = fileann.readlines()
                
                for t in textann:
                    # print('t: ',t)
                    a = t.split('\t')
                    # print("a: ")
                    if 'Person' in a[1] or 'PER' in a[1]:
                        Person.append(a[2].rstrip())
                        
                    
                    if 'Organization' in a[1] or 'ORG' in a[1]:
                        Org.append(a[2].rstrip())
        
        Person = list(dict.fromkeys(Person))
        Org = list(dict.fromkeys(Org))
        # print('Person: ',Person,'Org: ',Org)
        
        if hasann == True:
            for i in os.listdir(os.getcwd()):
                if i.endswith('.tei'):
                    author = authorName(i)
                    # print('author: ',author)
                    for i in os.listdir(os.getcwd()):
                        if i.endswith('.txt'):   
                            filei = open(i,'r',encoding='utf-8')
                            text = filei.read()
                            texti = tokenize(text)
                            texti = filter1(texti)
                            
                            result = perCounter(Person,[item for item in perNERString(texti) if item not in author])
                            print(Person)
                            print([item for item in perNERString(texti) if item not in author])
                            print(result)
                            bingoP+=result[3]
                            GTP+=result[4]
                            FDP+=result[5]
                            
                            
                            resultOrgLoose = orgCounter_loose(Org,orgNERString(texti))
                            print(Org)
                            print(orgNERString(texti))
                            print(resultOrgLoose)
                            
                            bingoOL += resultOrgLoose[3]
                            bingoOLp += resultOrgLoose[6]
                            GTOL += resultOrgLoose[4]
                            FDOL += resultOrgLoose[5]
                            
                            
                            resultOrgStrict = orgCounter_strict(Org,orgNERString(texti))
                            print(resultOrgStrict)
                            bingoOS += resultOrgStrict[3]
                            bingoOSp += resultOrgStrict[6]
                            GTOS += resultOrgStrict[4]
                            FDOS += resultOrgStrict[5]
        
    except:
        pass
    
print(bingoP,GTP,FDP)
print(bingoOL,GTOL,FDOL)
print(bingoOS,GTOS,FDOS)

recallPerson = bingoP/GTP
precisionPerson = bingoP/FDP
F1Person = (2*recallPerson*precisionPerson)/(recallPerson+precisionPerson)
print('Person recall = ', recallPerson, 'Person precision = ', precisionPerson, 'Person F1 = ', F1Person)

recallOrgL = bingoOL/GTOL
precisionOrgL = bingoOL/FDOL
F1OrgL = (2*recallOrgL*precisionOrgL)/(recallOrgL+precisionOrgL)
print('Orgloose recall = ', recallOrgL, 'Orgloose precision = ', precisionOrgL, 'Orgloose F1 = ',F1OrgL)

recallOrgS = bingoOS/GTOS
precisionOrgS = bingoOS/FDOS
F1OrgS = (2*recallOrgS*precisionOrgS)/(recallOrgS+precisionOrgS)
print('Orgstrict recall = ', recallOrgS, 'Orgstrict precision = ', precisionOrgS, 'Orgstrict F1 = ',F1OrgS)    
