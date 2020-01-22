from nltk.tokenize import sent_tokenize, word_tokenize
import pysbd


fileObj = open('standard.txt', 'r')
fileOut = open("standardToken.txt","w")
data = fileObj.read()
seg = pysbd.Segmenter(language="en", clean=False)   
text = seg.segment(data)

for t in text:
    if t == "":
        pass
    else:
        print(t+'\n')
    fileOut.write(t+'\n')

fileOut.close()
