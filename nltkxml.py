import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

fileObj = open('results.txt', 'r')
fileOut = open("resultsTokens.txt","w")
data = fileObj.read()
tokens = nltk.sent_tokenize(data)
tokens1 = str(tokens)
print(tokens1)
fileOut.write(tokens1)
fileOut.close()
