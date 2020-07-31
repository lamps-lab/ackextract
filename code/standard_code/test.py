from ackstanza2 import *

print(orgNER_Classifier(orgNER(XML2ack(grobid('Adams_JournExpSocPsych_2010_V85.pdf')))))

print(orgNER_Classifier(orgNER(XML2ack('Abendroth_AmSocioRev_2014_G8Lr.pdf.tei'))))


