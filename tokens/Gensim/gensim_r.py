from nltk.tokenize import sent_tokenize, word_tokenize
import gensim 
from gensim.summarization.textcleaner import split_sentences



fileObj = open('results.txt', 'r')
fileOut = open("resultsTokens.txt","w")
data = fileObj.read()
text = split_sentences(data)

for t in text:
    if t == "":
        pass
    else:
        print(t+'\n')
    fileOut.write(t+'\n')

fileOut.close()
