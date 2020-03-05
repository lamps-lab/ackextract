from ackseer import *
import os
import glob
import shutil
import time



# os.chdir(r'C:\PWang\Datasets\2ndGT')   去哪
# print(os.getcwd())                     当前目录
# print(os.listdir(os.getcwd()))         当前目录下的子目录

# traverse all XML
# path = r'C:\PWang\Datasets\Python\xmls'
# filex = open('paperchecklist.txt','w',encoding="utf-8")
# t = ''
# x = 0
# y = 0
# for i in os.listdir(path):
    # x+=1
    # if i.endswith('.tei'):
        
        # if XML2ack(path+'\\'+i)==[]:
            
            # continue
        # t = str(x)+','+str(i)+'\n'
        # y+=1
        # print(t)
        # filex.write(t)

# print('y= ',y,'x= ',x)


#traverse
#print([x[0] for x in os.walk(r'C:\PWang\Datasets\2ndGT')][1:])


#directory operation: unprocessed paper list textfile
# filep = open('checklist.txt','r',encoding="utf-8")
# filet = open('textlist.txt','w',encoding="utf-8")
# fileann = open('annlist.txt','w',encoding="utf-8")

# list = filep.readlines()
# a = 50
# for l in list: # l是tei
    # if l[0]!='\t':
        # a+=1
        
        
        
        # name = str(a)+l.split(',')[1]
        # nametxt = name[:-8]+'txt'+'\n'
        # nameann = name[:-8]+'ann'+'\n'
        # path = r"C:\PWang\Datasets\2ndGT\\"+name.rstrip()
        # print(path)   #path 是目录
        # filet.write(nametxt)
        # fileann.write(nameann)
        # print(name)
        
        
        
        
        
        
        # 一次性的
        # os.makedirs(path)  #造文件夹
        #复制
        # source = r"C:\PWang\Datasets\PDFS\\"
        # for i in os.listdir(source):
            # if l.find(i) != -1:
                # shutil.copyfile(source+str(i), path+'\\'+str(i))
        
        # time.sleep(1)
        
        # source2 = r"C:\PWang\Datasets\Python\xmls\\"
        # for j in os.listdir(source2):
            # if l.find(j) != -1:
                # shutil.copyfile(source2+str(j), path+'\\'+str(j))
        










