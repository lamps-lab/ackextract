# ackextract

Acknowledgement and its name entities extraction from scholarly papers. Implemented in Python.

Copyright (c) 2020, Jian Wu, Pei Wang

## Operating System: 
This code works on Windows and Linux so far, it should work on Mac as well

## Installation
### Dependencies: Make sure that both Python 3.0+ and Java 1.8+ are installed on your system. 
### Requirement: 
#### Install StanfordNLP(https://github.com/stanfordnlp),
#### Install Pragmatic Segmenter(https://pypi.org/project/pysbd/#files,) 
#### Install Grobid(https://github.com/kermitt2/grobid/releases), 
Grobid 0.5.5 works better so far.
go to grobid directory like C:\downloads\grobid-0.5.5\grobid-0.5.5
and run 
```
gradlew clean install
```
.

## Preparation:
Before importing ackeer.py, make sure running stanfordnlp server at first: 
### go to stanfordnlp directory
and run 
```
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
```
### go to grobid directory
and run
```
gradlew run
```
## Functions
Check the code and comments for more details

## brief example of implementation

