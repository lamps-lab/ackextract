import json

#with open('standardTokens.txt', 'r') as data_file:
#    json_data = data_file.read()
#    jdata = json.loads(json_data)
#    print(jdata)

fileObj = open('standardToken.txt', 'r')

#print(data)

sTokens = fileObj.readlines()
fileObj.close()
nums = len(sTokens)
print('# of standard tokens: ', nums)

fileObj = open('resultsTokensaftertrim.txt', 'r')
rTokens = fileObj.readlines()
fileObj.close()
numr = len(rTokens)
print('# of tokens from XMLs: ', numr)

n = 0
for s in sTokens:
    print(s)
    for r in rTokens:
       if r.find(s)!= -1:
           n = n + 1
           print ( n, r)
           break
    print('---------------------')
print('recall = ',"{:.0%}".format(n/nums) ) 
print('precision = ',"{:.0%}".format(n/numr) )

