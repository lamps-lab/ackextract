from xml.dom.minidom import parse
import re

pattern1 = re.compile('acknowledg|funding', re.IGNORECASE)
pattern2 = re.compile('thank[s]? |grateful|gratitude|funding', re.IGNORECASE)

def allChildren(node):
    content = ''
    nodelist = node.childNodes
    for node in nodelist:
        if node.nodeType != node.TEXT_NODE:
            content = content + allChildren(node)
        else:
            nodedata = node.data
            content = content + nodedata
    return content

print('Start:')

filer = open("xmlfilenames10.txt", "r")
filew = open("results.txt","w+")
n = 1
for fname in filer:
    hstr = str(n) + ': ' + fname.rstrip() + ' ================'
    print(hstr)
    #filew.write(hstr + '\n')
    n += 1
    pfname = 'xmls/' + fname.rstrip()
    temp_list = []
    try:
        doc = parse(pfname)
        divs = doc.getElementsByTagName('div')
        hasacknowledgement = 0
        for div in divs:
            divtype = div.getAttribute("type")
            if divtype == 'acknowledgement' or divtype == 'annex':
                div2s = div.getElementsByTagName('div')
                for div2 in div2s:
                    heads = div2.getElementsByTagName('head')
                    hashead = 0
                    for head in heads:
                        hashead = 1
                        ack = allChildren(head)
                        if pattern1.search(ack):
                            print (ack)
                            filew.write(ack + '\n')
                            ps = div2.getElementsByTagName('p')
                            for p in ps:
                                hasacknowledgement = 1
                                pdata = allChildren(p)
                                print(pdata)
                                temp_list.append(pdata)
                                filew.write(pdata + '\n')
                    if hashead == 0:
                        p0s = div2.getElementsByTagName('p')
                        for p0 in p0s:
                            p0data = allChildren(p0)
                            if pattern1.search(p0data):
                                hasacknowledgement = 1
                                print(p0data)
                                temp_list.append(p0data)
                                filew.write(p0data + '\n')
                                
        #if hasacknowledgement == 0:
        divs = doc.getElementsByTagName('div')
        for div in divs:
            ps = div.getElementsByTagName('p')
            for p in ps:
                pdata = allChildren(p)
                if pattern2.search(pdata):
                    saved = 0
                    for savedstr in temp_list:
                        if pdata == savedstr:
                            saved = 1
                            break
                    if saved == 0:
                        print(pdata)
                        temp_list.append(pdata)
                        filew.write(pdata + '\n')
                        
        notes = doc.getElementsByTagName('note')
        for note in notes:
            notedata = allChildren(note)
            if pattern2.search(notedata):
                print(notedata)
                filew.write(notedata + '\n')
        
        
    except Exception as e:
        print('XML document has error!')
        filew.write('XML document has error! ')
        #print(e.message)
    print('---------------------------------------------------\n')
    #filew.write('---------------------------------------------------\n\n')
filew.close()
