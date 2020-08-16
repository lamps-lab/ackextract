from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from xml.dom.minidom import parse
import re


def NERper(txt):
    ner=[]
    per=[]
    temp=[]
    
    ne_tree = nltk.ne_chunk(pos_tag(word_tokenize(txt)))
    for n in ne_tree:
        if isinstance(n, tuple):
            pass
        else:
            ner.append(n)
    
    for x in ner:
        if 'PERSON' in str(x):
            temp.append(x)
    for t in temp:
        name=''
        for a in t:
            name+=a[0]+' '
        per.append(name.strip())
    return per

def NERorg(txt):
    ner=[]
    org=[]
    temp=[]
    
    ne_tree = nltk.ne_chunk(pos_tag(word_tokenize(txt)))
    for n in ne_tree:
        if isinstance(n, tuple):
            pass
        else:
            ner.append(n)
    
    for x in ner:
        if 'ORGANIZATION' in str(x):
            temp.append(x)
    for t in temp:
        name=''
        for a in t:
            name+=a[0]+' '
        org.append(name.strip())
    return org
