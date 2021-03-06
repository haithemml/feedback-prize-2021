# -*- coding: utf-8 -*-
"""Feedback-Prize-2021

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KTU38mlF1343WSPnM6_0IP9W4Oui5Mfd
"""

pip install keras

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
#from sklearn import clean_text
from textblob import TextBlob
from nltk.corpus import stopwords
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# %matplotlib inline

df = pd.read_csv('drive/MyDrive/feedback/train.csv')
df

import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
import string

df.column = ['discourse_text']

string.punctuation

def remove_punct(text):
  text_nopunct = "".join([char for char in text if char not in string.punctuation])
  return text_nopunct

df['no_punct'] = df['discourse_text'].apply(lambda x: remove_punct(x))
df

import re

def tokenize(text):
  tokens = re.split('\n', text)
  return tokens

df['text_tokenized'] = df['discourse_text'].apply(lambda x: tokenize(x.lower()))
df

from nltk.corpus import stopwords
stopwords.words('english')

def remove_stopwords(text):
  text_nostop = [word for word in text if word not in stopwords.words('english')]
  return text_nostop

df['text_nostop'] = df['text_tokenized'].apply(lambda x: remove_stopwords(x))
df

df['discourse_type'].value_counts()

from collections import Counter

claim = []
evidence =[]
position=[]
concluding=[]
lead=[]
counterclaim=[]
rebuttal=[]
df.dropna(inplace=True)
# val for sublist in list of lists for val in sublist
writers = df[df['discourse_type']=='Claim']['text_nostop'].tolist()
claim.extend(writer for writer in writers)
claim = [val for sublist in claim for val in sublist]
argument_claim = Counter(claim)
print()
print(argument_claim.most_common()[:20])

writers = df[df['discourse_type']=='Evidence']['text_nostop'].tolist()
evidence.extend(writer for writer in writers)
evidence = [val for sublist in evidence for val in sublist]
argument_evidence = Counter(evidence)
print()
print(argument_evidence.most_common()[:20])

writers = df[df['discourse_type']=='Position']['text_nostop'].tolist()
position.extend(writer for writer in writers)
position = [val for sublist in position for val in sublist]
argument_position = Counter(position)
print()
print(argument_position.most_common()[:20])

writers = df[df['discourse_type']=='Concluding Statement']['text_nostop'].tolist()
concluding.extend(writer for writer in writers)
concluding = [val for sublist in concluding for val in sublist]
argument_concluding = Counter(concluding)
print()
print(argument_concluding.most_common()[:20])

writers = df[df['discourse_type']=='Lead']['text_nostop'].tolist()
lead.extend(writer for writer in writers)
lead = [val for sublist in lead for val in sublist]
argument_lead = Counter(lead)
print()
print(argument_lead.most_common()[:20])

writers = df[df['discourse_type']=='Counterclaim']['text_nostop'].tolist()
counterclaim.extend(writer for writer in writers)
counterclaim = [val for sublist in counterclaim for val in sublist]
argument_counterclaim = Counter(counterclaim)
print()
print(argument_counterclaim.most_common()[:20])

writers = df[df['discourse_type']=='Rebuttal']['text_nostop'].tolist()
rebuttal.extend(writer for writer in writers)
rebuttal = [val for sublist in rebuttal for val in sublist]
argument_rebuttal = Counter(rebuttal)
print()
print(argument_rebuttal.most_common()[:20])

common1 = [word[0] for word in [claim for claim in argument_claim.most_common()[:20]]]
common2 = [word[0] for word in [evidence for evidence in argument_evidence.most_common()[:20]]]
common3 = [word[0] for word in [position for position in argument_position.most_common()[:20]]]
common4 = [word[0] for word in [concluding for concluding in argument_concluding.most_common()[:20]]]
common5 = [word[0] for word in [lead for lead in argument_lead.most_common()[:20]]]
common5 = [word[0] for word in [counterclaim for counterclaim in argument_counterclaim.most_common()[:20]]]
common6 = [word[0] for word in [rebuttal for rebuttal in argument_rebuttal.most_common()[:20]]]
print()
print(len(argument_claim))
print(len(argument_evidence))
print(len(argument_position))
print(len(argument_concluding))
print(len(argument_lead))
print(len(argument_counterclaim))
print(len(argument_rebuttal))

df['discourse_end'].plot(kind='hist')

df.dropna(inplace=True)

df['discourse_start'].plot(kind='hist')