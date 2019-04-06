# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:45:27 2019

@author: Mads
"""

import numpy as np
import random
import wikipedia as wiki

def getWikiData(freq_keyword,all_keywords,version):
    if version == 1:
        prKeyword =3 
        wikiPages = []
        for i in freq_keyword:
            wikiPages.append(wiki.search(i,results=prKeyword))
        
        bestMatch = {"row":0,"column":0,"word":'hi'}
        maximum = 0
        for i in range(len(freq_keyword)):
            for j in range(prKeyword):
                try:
                    document = wiki.summary('{:}'.format(wikiPages[i][j]))
                    current_co = covarianceDocKey(document,all_keywords)
                    if current_co > maximum:
                        maximum = current_co
                        bestMatch['row'],bestMatch['column'],bestMatch['word'] = i,j,wikiPages[bestMatch['row']][bestMatch['column']]
                        
                except:
                    continue
        print('Title of best match: ',bestMatch['word'])
        return wiki.summary(wikiPages[bestMatch['row']][bestMatch['column']])
    else:
        return wiki.summary(freq_keyword[0])


def covarianceDocKey(document,keywords):
    #Get the keyphrases
    #I need the counts from the first input 
    random_genKeyCount = np.ones((16))
#    random_genKeyCount =np.array([random.randrange(1, 5, 1) for _ in range(16)])
    words = document.split(" ")
    keyword_count = np.zeros((len(keywords)))
    for i,word in enumerate(words):
        if word in keywords:
            keyword_count[keywords.index(word)]+=1    
    return np.matmul(keyword_count,random_genKeyCount.T)
            
            

        
    
def most_freq_keyword(keywords):
    words, count = np.unique(keywords, return_counts=True)
    max_counts = np.sort(count)[::-1]

    new_keywords = []
    for i in range(3):
#        i.append(np.where(max_counts[i]==count))
        index = np.where(max_counts[i]==count)[0]
        
        n = 0
        while n < len(index):
            if words[index[n]] not in new_keywords:
                element = words[index[n]]
                new_keywords.append(element)
                break
            n+= 1
    return new_keywords
#keywords = ['dog','dog','cat','dog','c','dog','r','e','q','e','q','p']
keywords = ["evolution of dogs","instincts","distinct breeds","humans","new breeds","distinct societal needs","hunters","keen senses of sight","major role","rudimentary form of genetic engineering","gray wolf","earliest encounters","Human beings","smell","desire","details"]
freq_keywords = most_freq_keyword(keywords)

#version 0 = simple, no covariance between keywords and documents. version = 1, covariance is calculated.
version = 1
docs = getWikiData(freq_keywords,keywords,version)
print(docs)

