# ackextract

Acknowledgement and its name entities extraction from scholarly papers. Implemented in Python.

Copyright (c) 2020, Jian Wu, Pei Wang

## Installation
Dependencies: Make sure that both Python 3.0+ and Java 1.8+ are installed on your system. 
Requirement: Make sure StanfordNLP(https://github.com/stanfordnlp), Pragmatic Segmenter(https://pypi.org/project/pysbd/#files,) and Grobid(https://grobid.readthedocs.io/en/latest/Install-Grobid/) are installed as well

## Operating System: 
This code works on Windows and Linux so far, it should work on Mac as well.

## Preparation:
Before importing ackeer.py, make sure running stanfordnlp server at first: 
go to stanfordnlp directory
and run 
```
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
```
## Functions
Check the code and comments for more details
