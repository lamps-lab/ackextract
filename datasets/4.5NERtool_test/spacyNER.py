import en_core_web_sm

nlp = en_core_web_sm.load()   


# for X in doc.ents:
    # print(X.text, X.label_) 
    # filew.write(X.text+'\t'+X.label_+'\n')

 
def NERper(txt):
    
    per=[]
    
    
    doc = nlp(txt)
    for X in doc.ents:
        if X.label_=='PERSON':
            per.append(X.text)
    
    return per

def NERorg(txt):
    
    org=[]
    
    
    doc = nlp(txt)
    for X in doc.ents:
        if X.label_=='ORG':
            org.append(X.text)
    
    return org
    