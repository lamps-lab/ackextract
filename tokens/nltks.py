import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

fileObj = open('standard.txt', 'r')
fileOut = open("standardTokens.txt","w")
data = fileObj.read()
tokens = nltk.sent_tokenize(data)
#tokens1 = str(tokens)
for t in tokens:
    
    print(t+'\n')
    fileOut.write(t+'\n')

fileOut.close()
