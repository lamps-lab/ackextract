from xml.dom.minidom import parse
import re

pattern = re.compile('thank[s]? |acknowledge|grateful|gratitude', re.IGNORECASE)
            
def allChildren(node):
    nodelist = node.childNodes
    for node in nodelist:
        if node.nodeType != node.TEXT_NODE:
            allChildren(node)
        else:
            nodedata = node.data.strip()
            if len(nodedata) > 0 and pattern.search(nodedata):
                print(node.data)

print('Start:')

file = open("xmlfilenames.txt", "r")
n = 1
for fname in file:
    print (str(n) + ': ' + fname.rstrip() + ' ================')
    n += 1
    pfname = 'xmls/' + fname.rstrip()
    try:
        doc = parse(pfname)
        teis = doc.getElementsByTagName('TEI')
        for tei in teis:
            allChildren(tei)
    except:
        print('XML document has error!')
    print ('---------------------------------------------------\n')

