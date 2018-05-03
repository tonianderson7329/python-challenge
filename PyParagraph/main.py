import os
import csv
import re

filepath = os.path.join("PyParagraph", "paragraph_1.txt")
nwords=0
SenCount=0
# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        Countwords=line.split()

    for re in reader:    
        Sentence_count = re.split("(?&lt;=[.!?]) +", reader)

        nwords+=len(Countwords)
        SenCount+=len(Sentence_count)

        print(nwords)
        print(SenCount)
   

