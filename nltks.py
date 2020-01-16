import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

fileObj = open('standard.txt', 'r')
data = fileObj.read()
tokens = nltk.sent_tokenize(data)
tokens1 = str(tokens)
print(tokens1)
fileOut = open("standardTokens.txt","w")
fileOut.write(tokens1)
fileOut.close()
