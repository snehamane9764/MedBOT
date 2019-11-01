import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np
import json
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import random
import os
#new libraries
import difflib
print('Can you please discribe your Symptoms')

sr = os.path.join('C:/Users/Lenovo/Desktop/medbot/final dataset.csv')
ab = np.array(sr)
for ab in range(1,3):
	for j in range(ab):
		 print()
dis = np.array(ab)
symp = np.array(ab)

#def stopWords(text):
    #text is a sentence
    #stopw = set(stopwords.words('english'))
 #   filtered = []
  #  words = word_tokenize(text)
   # for i in words:
    #    if i not in stopw:
     #       filtered.append(i)
   # return filtered

#def stemming(text):
    #text could be a sent or word
 #   ps = PorterStemmer()
  #  empty = []
   # for w in text:
    #    empty.append(w)
    #return empty

def getSymptoms():
   # print('Please tell me about your symptoms')
    inp = raw_input('Please tell me about your symptoms')
    #sent = sent_tokenize(inp)
    #filt = stopWords(inp)
   
#compare input with csv file with filtered sentence
    i1=i2=i3=0
    max1=0
    max2=1
    max3=2
for i in range(1,11):
	for j in range(ab):
			
			sequence = difflib.SequenceMatcher(isjunk=None, a=dis[i], b=symp[j])
			diff = sequence.ratio()*100
        if(diff>max1):
            max3=max2
            max2=max1
            max1=diff
            i1=i
        elif(diff>max2):
            max3=max2
            max2=diff
            i2=i
        elif(diff>max3):
            max3=diff
            i3=i

	print('Diagnosed Diseases are:')
	    #if(i1!=i2!=i3):
	print(dis[i1])
	print(dis[i2])
	print(dis[i3])
	print(dis[i1])
               
     
	 
symp = getSymptoms()


