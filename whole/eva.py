from ackseer import *
import os
import glob

# countertest
rc = []
pr = []


m = 0
GT = 0
FD = 0


rcos = []
pros = []


ms = 0
ns = 0
GTs = 0
FDs = 0

rcol = []
prol = []


ml = 0
nl = 0
GTl = 0
FDl = 0

for f in [x[0] for x in os.walk(r'C:\PWang\Datasets\2ndGT')][1:]:
    os.chdir(f) 
    
    # person
    try:
        file1 = open('PER.txt','r',encoding="utf-8")
        list1 = file1.readlines()
        for i in os.listdir(os.getcwd()):
            if i.endswith('.tei'):
                print(XML2ack(i))
                print(ackPerExtract(i))
                result = perCounter(list1,ackPerExtractPure(i))
                print (result)
                if result[0]!= None:
                    rc.append(result[0])
                if result[1]!= None:
                    pr.append(result[1])
                              
                m+=result[3]
            
                GT+=result[4]
                FD+=result[5]
            
    except:
        continue
            
            
    # organization strict
    try:
        file2 = open('ORG.txt','r',encoding="utf-8")
        list2 = file2.readlines()
        for i in os.listdir(os.getcwd()):
            if i.endswith('.tei'):
                
                print(ackOrgExtract(i))
                results = orgCounter_strict(list2,ackOrgExtractPure(i))
                print (results)
                if results[0]!= None:
                    rcos.append(results[0])
                if results[1]!= None:
                    pros.append(results[1])
                
                
                ms+=results[3]
                ns+=results[6]
                GTs+=results[4]
                FDs+=results[5]
    except:
        continue
    
    # organization loose    
    try:
        file2 = open('ORG.txt','r',encoding="utf-8")
        list2 = file2.readlines()
        for i in os.listdir(os.getcwd()):
            if i.endswith('.tei'):
                
                print(ackOrgExtract(i))
                resultl = orgCounter_loose(list2,ackOrgExtractPure(i))
                print (resultl)
                if resultl[0]!= None:
                    rcol.append(resultl[0])
                if resultl[1]!= None:
                    prol.append(resultl[1])
                
                
                ml+=resultl[3]
                nl+=results[6]
                GTl+=resultl[4]
                FDl+=resultl[5]
    except:
        continue
         


microRecallPerson = m/GT
microPrecisionPerson = m/FD


microRecallOrgLoose = ml/GTl
microPrecisionOrgLoose = nl/FDl


 
microRecallOrgStrict = ms/GTs
microPrecisionOrgStrict = ns/FDs

print(m,GT,FD)
print(ml,GTl,FDl)
print(ms,GTs,FDs)

# print('PERSON ENTITY','\n','macro recall= ',str(macroRecallPerson*100)+'%','macro precision= ',str(macroPrecisionPerson*100)+'%','macro F1= ',(2*macroRecallPerson*macroPrecisionPerson)/(macroRecallPerson+macroPrecisionPerson))
print('PERSON ENTITY','\n','micro recall= ',microRecallPerson,'micro precision= ', microPrecisionPerson, 'microF1= ', (2*microRecallPerson*microPrecisionPerson)/(microRecallPerson+microPrecisionPerson))

# print('Loose ORG ENTITY','\n','macro recall= ',str(macroRcOrgLoose*100)+'%','macro precision= ',str(macroPcOrgLoose*100)+'%','macro F1= ',(2*macroRcOrgLoose*macroPcOrgLoose)/(macroRcOrgLoose+macroPcOrgLoose))
print('Loose ORG ENTITY','\n','micro recall= ',microRecallOrgLoose,'micro precision= ', microPrecisionOrgLoose, 'microF1= ', (2*microRecallOrgLoose*microPrecisionOrgLoose)/(microRecallOrgLoose+microPrecisionOrgLoose))

# print('Strict ORG ENTITY','\n','macro recall= ',str(macroRcOrgStrict*100)+'%','macro precision= ',str(macroPcOrgSrtict*100)+'%','macro F1= ',(2*macroRcOrgStrict*macroPcOrgSrtict)/(macroRcOrgStrict+macroPcOrgSrtict))
print('Strict ORG ENTITY','\n','micro recall= ',microRecallOrgStrict,'micro precision= ', microPrecisionOrgStrict, 'microF1= ', (2*microRecallOrgStrict*microPrecisionOrgStrict)/(microRecallOrgStrict+microPrecisionOrgStrict))

