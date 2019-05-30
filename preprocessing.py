# -*- coding: utf-8 -*-
"""Preprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qer2LUbkGUPN-ncdLqJjnRJkCO5HCNER
"""

import numpy as np
import pandas as pd

df = pd.read_csv("bitcoin_tweets.csv")

df=df.reset_index(drop=True)

t=df['timestamp']

date=[]
for i in range(len(t)):
    try:
        date.append(t[i][0:10])
    except:
        print(t[i])

publish_time=[]
for i in range(len(t)):
    try:
        publish_time.append(t[i][-8:])
    except:
        print(t[i])

df['publish_time']=publish_time
df['date']=date

ret=[]
for x in time:
    y = df[df['date']==x]
    y = y.sort_values(by=['retweets'], ascending = False)
    top10 = y[:10]
    r = top10['retweets']
    arr = r.values.copy()
    arr.resize(1, 10)
    ret.append(list(arr[0]))

rt = pd.DataFrame(ret,columns = ['rt1','rt2','rt3','rt4','rt5','rt6','rt7','rt8','rt9','rt10'])

cont=[]
for x in time:
    y = df[df['date']==x]
    y = y.sort_values(by=['retweets'], ascending = False)
    top10 = y[:10]
    r = top10['text']
    arr = r.values.copy()
    arr.resize(1, 10)
    cont.append(list(arr[0]))

cot = pd.DataFrame(cont,columns = ['ct1','ct2','ct3','ct4','ct5','ct6','ct7','ct8','ct9','ct10'])

time = pd.DataFrame(time,columns = ['date'])

k = pd.concat([time,cot,rt],axis = 1)

k.to_csv("tweets_dataset.csv",index = False)