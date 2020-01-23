
import pysbd 




fileObj = open('results.txt', 'r')
fileOut = open("resultsTokens.txt","w")
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
