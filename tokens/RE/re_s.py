import re
from nltk.tokenize import sent_tokenize, word_tokenize


fileObj = open('standard.txt', 'r')
fileOut = open("standardToken.txt","w")
data = fileObj.read()
tokens = re.split('[.?!][ \n]|\n+',data)
print(tokens)
for t in tokens:
    if t == "":
        pass
    else:
        print(t+'\n')
    fileOut.write(t+'\n')

fileOut.close()
