import json

#with open('standardTokens.txt', 'r') as data_file:
#    json_data = data_file.read()
#    jdata = json.loads(json_data)
#    print(jdata)

fileObj = open('standardTokens.txt', 'r')
data = fileObj.read()
#print(data)
data = data.replace("['", "")
data = data.replace("']", "")
sTokens = data.split("', '")
#for d in sTokens:
#   print(d)
fileObj.close()
nums = len(sTokens)
print('# of standard tokens: ', nums)

fileObj = open('resultsTokens.txt', 'r')
data = fileObj.read()
#print(data)
data = data.replace("['", "")
data = data.replace("']", "")
rTokens = data.split("', '")
#for d in rTokens:
#    print(d)
#    print('=======================')
fileObj.close()
numr = len(rTokens)
print('# of tokens from XMLs: ', numr)

n = 0
for s in sTokens:
    print(s)
    for r in rTokens:
       if r.find(s):
           n = n + 1
           print (n, r)
           break
    print('---------------------')
print('recall = ',"{:.0%}".format(n/nums) ) 
print('precision = ',"{:.0%}".format(n/numr) )

