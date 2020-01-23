from xml.dom.minidom import parse
import re

pattern = re.compile('thank[s]? |grateful|gratitude|fund|acknowledg|indebted|helpful|support', re.IGNORECASE)


filer = open("resultsTokens_re.txt", "r")
filew = open("resultsTokensaftertrim.txt","w+")
n = 1
data = filer.readlines()
#print(data)

x = 0
for r in data:
    
    if pattern.search(r):
        print(x+1,' ',r,'\n')
        x+=1
        filew.write(r )
filew.close()
