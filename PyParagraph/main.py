import csv
import os
import re

filepath = os.path.join("PyParagraph","paragraph_2.txt")
nwords = 0
sencount = 0
wordcounts = []
lettercount = 0
# Read data into from Text file
with open(filepath, 'r') as txtfile:
    for word in txtfile:
        #Split each word according to space
        Countwords=word.split(' ')
        #Counts the number of words
        nwords += len(Countwords)
       #Splits sentences according punctuations
        sentences = re.split("(?<=[.!?]) +", word)
       #Counts the approx. number of sentences
        sencount += len(sentences)
    #Retrives the average character oe letter count in a word
    Average = (nwords) / (len(Countwords))
#Read data into the Paragragh file
with open(filepath) as parfile:
    for sentence in parfile:
        #Identifies all words according to space into a varaible
        allwords = sentence.split(' ')
        #Counts all words that will append into a list
        wordcounts.append(len(allwords))
 #Takes the total word counts and divides by length       
avg_word = sum(wordcounts)/len(wordcounts)



print("Approx. Word Count:", + (nwords))
print("Approx. Sentence Count:", + (sencount))
print("Average Letter Count:", + (Average))
print("Average Sentence Length:", + (avg_word))