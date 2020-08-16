
import re

pattern3 = re.compile('(funding|grant)(.{0,20}) (:|support|came|assistance|was provided by)|(support(.{0,20})with|supported (in part )?by|support (from|of)|financed by|support(.{0,30})provided by|provided support|acknowledg)(.{0,120})(grant|scholarship|office|university|Council|assistance|constructive|fellowship|center|Foundation|Institut|fund|financial)|(work|paper|study) was supported in part by|(helpful|useful) (comments|feedback|suggest)|provide(d|s)?(.{0,25}) (fund|feedback|comment)|benefit(ed|s)?(.{0,15})from (.{0,60})(contribution|comment|insight)', re.IGNORECASE) 
pattern4 = re.compile('thank(?! you!)|appreciate|grateful (to|for)|gratitude to|like[s]? to acknowledge|indebted to|funded (by|in|through)|funds were provided by|(center|Foundation|Institut|university)(.{0,20})(provided(.{0,20})support|funded this)|financial(ly)? support', re.IGNORECASE) 

# pattern = re.compile('thank|grateful|gratitude|funded|funding|acknowledg|indebted|helpful|support|benefit|dedicated|useful|provided|assistance', re.IGNORECASE)    #feedback provided strengthened 

file = open(r'C:\PWang\Datasets\whole\sentencesclasstest\set.txt',encoding='utf-8')

data = file.readlines()
# print(data)
data2 =  [x.split('\t')[0] for x in data]
# print(data2)

GT2=[0,0]

# print(res)
right=0
false=0
for d in data:

    
    st=d.split('\t')[0]
    tag=d.split('\t')[1].strip()
    
    if tag == '1':
        GT2[0]+=1
    else :
        GT2[1]+=1
        
    if (pattern3.search(st)!=None or pattern4.search(st)!=None) and tag =='1':
        right+=1
    elif pattern3.search(st)==None and pattern4.search(st)==None and tag=='0':
        right+=1
    else:
        false+=1
        print(d)
    
print(GT2)  
print(right,false)

