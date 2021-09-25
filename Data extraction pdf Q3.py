#!/usr/bin/env python
# coding: utf-8

# In[13]:


get_ipython().system('pip install PyPDF2')
import PyPDF2 as p2
import pandas as pd
import numpy as np
import re


# In[16]:


PDFfile = open("PreScreen_DSAI_r3.pdf","rb")
pdfread = p2.PdfFileReader(PDFfile)
num_pages=pdfread.numPages
print("number of pages is : ",num_pages)

### extract 3rd page ###
x=pdfread.getPage(2)
print(x.extractText())


# # Question 3a.

# In[132]:


#source: https://stackoverflow.com/questions/52348119/probability-of-each-words-in-a-sentence

def tokenize(string):
    return re.compile('\w+').findall(string)

from collections import Counter

def word_freq(string): 
    text = tokenize(string.lower())
    c = Counter(text)           # count the words
    d = Counter(''.join(text))  # count all letters
    return (dict(c),dict(d))    # return a tuple of counted words and letters

#data = "This is a text, it contains  dupes and more dupes and dupes of dupes and lkkk."
data=input("Enter Paragraphs: " "\n")
data=data.lower()
#l=user_str.split()
words, letters = word_freq(data) # count and get dicts with counts

sumWords = sum(words.values())       # sum total words
sumLetters = sum(letters.values())   # sum total letters

# calc / print probability of word
for w in words:
    print("\n" "Probability of '{}': {}".format(w,words[w]/sumWords))

# calc / print probability of letter
#for l in letters:
#    print("Probability of '{}': {}".format(l,letters[l]/sumLetters))


# # 3b.

# In[133]:


#source: https://code.tutsplus.com/tutorials/counting-word-frequency-in-a-file-using-python--cms-25965

import re
import string

frequency = {}

data=input('Enter Paragraphs: ' "\n")
data=data.lower()
#l=user_str.split()
words, letters = word_freq(data) # count and get dicts with counts

#document_text = open("", 'r')
#text_string = data.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', data)

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
    
frequency_list = frequency.keys()
print("\n")
for words in frequency_list:
    print(words, frequency[words])


# # 3c.

# In[137]:


#source: https://www.codegrepper.com/code-examples/python/python+program+to+count+the+occurrences+of+each+word+in+a+given+string+sentence

# define string
#string = "data analytics is data analytics, isn't it data analytics?"
#def countOccurrences(str, word):
  
#    wordslist = list(str.split())
#    return wordslist.count(word)
  
str=input("Enter Paragraphs: " "\n")
str=str.upper()
substring = "DATA ANALYTICS"
#l=user_str.split()
#words, letters = word_freq(data) # count and get dicts with counts  
# Driver code
#str = "GeeksforGeeks A computer science portal for geeks  "
#word = "analytics"
#print("\n","number of the words",word,"appear in paragraph is : ",countOccurrences(str, substring))




count = str.count(substring)

# print count
print("\n""The count of",substring, "is:", count)

