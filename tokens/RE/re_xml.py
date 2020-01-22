import re
from nltk.tokenize import sent_tokenize, word_tokenize


fileObj = open('results.txt', 'r')
fileOut = open("resultsTokens_re.txt","w")
data = fileObj.read()
print(data)
tokens = re.split('[.?!][ \n]|\n+',data)
for t in tokens:
    print(t+'\n')
    fileOut.write(t+'\n')
fileOut.write(tokens1)
fileOut.close()
