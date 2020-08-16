

file1 = open (r'C:\PWang\Datasets\whole\sentencesegtest\GT2.txt','r',encoding='utf-8')
file2 = open (r'C:\PWang\Datasets\whole\sentencesegtest\sampleset2.txt','r',encoding='utf-8')
GT=[]
for f in file1.readlines():
    GT.append(f.strip(' \n'))
res= file2.read()



# Pragmatic
# import pysbd
# def tokenize(text):
    # seg = pysbd.Segmenter(language="en", clean=False)
    # return seg.segment(text)
# res2=tokenize(res) 



# stanza
# import stanza
# nlp = stanza.Pipeline(lang='en', processors='tokenize,ner')
# def tokenize(text):  
    # textnlp = nlp(text)
    # return [sentence.text for sentence in textnlp.sentences]
# res2=tokenize(res) 






# nltk
# import nltk
# from nltk.tokenize import sent_tokenize, word_tokenize
# res2 = nltk.sent_tokenize(res) 



# Gensim
# import gensim 
# from gensim.summarization.textcleaner import split_sentences
# res2 = split_sentences(res)  



# for g in GT:
    # print(g,'\n')
# print(GT)
# print(res)


a=0
b=0
c=0
d=0
for x in res2:
    if x in GT:
        a+=1
    else:
        print(x)
    b+=1
print(a,b)

for x in GT:
    if x in res2:
        c+=1
    # else:
        # print(x)
    d+=1
print(c,d)