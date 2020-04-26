# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 22:00:31 2020
@author: nicob
"""
"""
While trying to solve a German language exercise that requested to guess some words with missing letters, kind of crossword,
I thought it was a good idea to get a shortlist from automated help.

The German dictionary I found online is not the best one, there are some missing words.

"""

# Input Name=1 if the searched word is a name or 0 if it's an adjective
# x is the searched word, any unknown letter must be entered as _ (underscore)
Nome=1
x='H_us'

import itertools as it

# read in the German dictionary
v=open('deutsch.txt')
l=v.read()
voc=l.split()

alp='a b c d e f g h i j k l m n o p q r s t u v wx y z ä ö ü ß'
alp1=alp.upper()
lalp=alp.split()
lalp1=alp1.split()


# create the list of missing letters and calculate its lenght
y=[]
for i in range (len(x)):
    if x[i]=='_':
        y.append(i)
    else:
        i=i+1       
print (y)
l=len(y)


# create all combinations of n=len(y) letters for small and capital
comb1=[p for p in it.product(lalp, repeat=l)]
comb2=[p for p in it.product(lalp1, repeat=l)]


#short list of the words with same lenght and initial letter, if known, of the searched one
def selist (z):
    vocs=[]
    for i in range (len(voc)):
        if len(voc[i])==len(z) and x[0]=='_':
            vocs.append(voc[i])
        else: 
           if len(voc[i])==len(z) and (voc[i][0]==z[0] or voc[i][0]==z[0].upper() or voc[i][0]==z[0].lower()):
             vocs.append(voc[i])
           else:
            voc[i-1]=voc[i]
    print(len(vocs))
    return vocs

f=selist(x)


#returns the list of the words where _ is replaced by the combinations of letters
def porc(x,k):
    x1=''
    w=[]
    j=0
    for i in range (len(x)):
        if x[i]=='_' and Nome==1 and i==0:
            w.append(comb2[k][j])
            j=j+1
        elif x[i]=='_':
            w.append(comb1[k][j])
            j=j+1
        else:
           w.append(x[i])
    for z in range (len(w)):
      x1=x1+w[z]
    return x1  


#checks the list x1 against the shortlist of exsisting words f and returns all the possibe words that include the searched one
def find (x):
    s=[]
    for k in range (len(comb1)):
          if porc(x,k) in f:
              s.append(porc(x,k))
          else:
            k=k+1
    print(s)
    return s

find(x)


    