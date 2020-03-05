from ackseer import *
import os
import glob

p=0
o = 0
orgdict={}
for f in [x[0] for x in os.walk(r'C:\PWang\Datasets\2ndGT')][1:]:
    os.chdir(f) 
    try:
        file1 = open('ORG.txt','r',encoding="utf-8")
        list1 = file1.readlines()
        list1 = list(dict.fromkeys(list1))
        for l in list1:
            o+=1
            if l.strip() not in orgdict:
                orgdict[l.strip()] = [1]
            
            elif l.strip() in orgdict:
                orgdict.get(l.strip())[0]+=1
                
        p+=1
        
    except:
        pass

for f in [x[0] for x in os.walk(r'C:\PWang\Datasets\2ndGT')][1:]:
    os.chdir(f) 
    try:
        for i in os.listdir(os.getcwd()):
            if i.endswith('.ann'):                
                fileann = open(i,'r',encoding='utf-8')
                listann = fileann.readlines()
                listann = list(dict.fromkeys(listann))
                for l in listann:
                    
                    if 'Organization' in l or 'ORG'in l:
                        o+=1
                        x = l.split('\t')[2]
                        print(x)
                        if x.strip() not in orgdict:
                            orgdict[x.strip()] = [1]
                
                        elif x.strip() in orgdict:
                            orgdict.get(x.strip())[0]+=1
                            
        p+=1

    except:
        pass

result = {k: v for k, v in sorted(orgdict.items(), key=lambda item: item[1],reverse=True)}     
print(result,p,o)