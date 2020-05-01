# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 23:06:46 2020

@author: nicob
"""
"""
While trying to solve a German language exercise that requested to guess some words with missing letters, kind of crossword,
I thought it was a good idea to get a shortlist from automated help.

The German dictionary I found online is not the best one, there are some missing words.
"""

# x is the searched word, any unknown letter must be entered as _ (underscore)
x='H_________r'

import itertools as it

# read in the German dictionary
v=open('deutsch.txt')
l=v.read()
voc=l.split()

#alp='a b c d e f g h i j k l m n o p q r s t u v wx y z ä ö ü ß'



# create the list of missing letters and calculate its lenght
y=[]
d={}
for i in range (len(x)):
    if x[i]!='_':
        y.append(i)
        d[i]=x[i]
    else:
        i=i+1       
#print (y)
#l=len(y)
#print(d)

#short list of the words with same lenght and initial letter of the searched one, if knwon
def selist (z):
    vocs=[]
    for i in range (len(voc)):
        if len(voc[i])==len(z) and x[0]=='_':
            vocs.append(voc[i])
        else: 
           if len(voc[i])==len(z) and voc[i][0]==z[0]: #or voc[i][0]==z[0].upper() or voc[i][0]==z[0].lower()):
             vocs.append(voc[i])
           else:
            voc[i-1]=voc[i]
#    print(len(vocs))
    return vocs

f=selist(x)

# final shortlist    
L=[]
for k in f:
  l=[]  
  for i in y:
    if k[i]==d[i] and k.find(k[i])==i:
        l.append(i)
    else:
        l.append('false')
  if l==y:
     L.append(k)
print(L)   

    

        




  

        
