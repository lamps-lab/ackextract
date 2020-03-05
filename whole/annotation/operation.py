import os
filet = open('textlist.txt','r',encoding="utf-8")
fileann = open('annlist.txt','r',encoding="utf-8")
t = filet.readlines()
ann = fileann.readlines()
for t0 in t:
    
    with open(t0.rstrip(),'w') as t1:
        pass

for a0 in ann:
    
    with open(a0.rstrip(),'w') as a1:
        pass