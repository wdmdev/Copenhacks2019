# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:45:27 2019

@author: Mads
"""

import numpy as np
import wikipedia as wiki
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


def getWikiData(freq_keyword,all_keywords,version):
    if version == 1:
        prKeyword =3 
        wikiPages = []
        for i in freq_keyword.keys():
            wikiPages.append(wiki.search(i,results=prKeyword))
        
        bestMatch = {"row":0,"column":0,"word":'blank'}
        maximum = 0
        for i in range(len(freq_keyword)):
            for j in range(prKeyword):
                try:
                    document = wiki.summary('{:}'.format(wikiPages[i][j]))
                    current_co = covarianceDocKey(document,all_keywords,freq_keyword)
                    if current_co > maximum:
                        maximum = current_co
                        bestMatch['row'],bestMatch['column'],bestMatch['word'] = i,j,wikiPages[bestMatch['row']][bestMatch['column']]
                        
                except:
                    continue
        title = wikiPages[bestMatch['row']][bestMatch['column']]
#        wikiPageData = wiki.WikipediaPage(title)
#        print(title)
#        print(wikiPageData.sections)   
#        print(wikiPageData.categories)
#        print(wikiPageData.content)
        
        print('Title of best match: ',title)
        return title,all_keywords
    else:
        return wikiPages[freq_keyword.values()[0]],all_keywords


def covarianceDocKey(document,keywords, freq_keywords):
    #Get the keyphrases
    #I need the counts from the first input 
    vektor_transcript = np.zeros((len(keywords)))
    
    for i, k in enumerate(keywords):
        if k in freq_keywords:
            vektor_transcript[i] = freq_keywords[k]
            
    
#    random_genKeyCount =np.array([random.randrange(1, 5, 1) for _ in range(16)])
    words = document.split(" ")
    keyword_count = np.zeros((len(keywords)))
    for i, word in enumerate(words):
        if word in keywords:
            keyword_count[keywords.index(word)]+=1   
            
    return np.matmul(keyword_count,vektor_transcript.T)
            
            

        
    
def most_freq_keyword(transcript,keywords):
    ps = PorterStemmer()
    
    words, count = np.unique(transcript.split(" "), return_counts=True)
    for i, word in enumerate(words):
        if isinstance(words[i], str):
            words[i] = ps.stem(words[i])
            words[i] = words[i].lower()
    tempArr = {}
    
    for i, keyword in enumerate(keywords):
        if isinstance(keyword, str):
            keywords[i] = keyword.lower()
#            if(len(keyword) ==1):
            keywords[i] = ps.stem(keyword)
        
    for i, word in enumerate(words):
        if word in keywords:
           tempArr[word] = count[i]
            
            
#    max_counts = np.sort(count)[::-1]
    
    temp = np.sort(list(tempArr.values()))[::-1]
    
    
    
    new_keywords = []
    if len(tempArr) < 3:
        n = len(tempArr)
    else:
        n = 3

    for keyphrase, value in tempArr.items():
        if value in temp[:n]:
            new_keywords.append(keyphrase)

    
#    if len(temp) < 3:
#        n = len(keywords)
#    else:
#        n = 3
#    for i in range(n):
#        
#        new_keywords = new_keywords.append()
#        
#        index = np.where(max_counts[i]==count)[0]
#        
#        n = 0
#        while n < len(index):
#            if words[index[n]] not in new_keywords:
#                element = words[index[n]]
#                new_keywords.append(element)
#                break
#            n+= 1
    return dict(zip(new_keywords, temp[:n]))
#keywords = ['dog','dog','cat','dog','c','dog','r','e','q','e','q','p']
#keywords = [
#        "opera performances",
#        "term opera house",
#        "public opera house",
#        "world's oldest working opera house",
#        "large number of working opera houses",
#        "Early United States opera houses",
#        "Teatro Massimo",
#        "Teatro San Cassiano",
#        "wealthy people",
#        "large performing-arts center",
#        "theatre building",
#        "patronage system",
#        "Italy",
#        "operas",
#        "centuries",
#        "supported system",
#        "larger performing arts centers",
#        "San Carlo",
#        "ordinary people",
#        "theatre companies",
#        "social position",
#        "wealthy patrons",
#        "term of prestige",
#        "capitalist social forms",
#        "cities",
#        "Naples",
#        "variety of functions",
#        "ticket sales",
#        "audience seating",
#        "towns",
#        "institutional grants",
#        "backstage facilities",
#        "hosting community dances",
#        "fairs",
#        "combination of government",
#        "century",
#        "rulers",
#        "orchestra pit",
#        "Henry Purcell",
#        "rise of bourgeois",
#        "funds",
#        "costumes",
#        "European culture",
#        "political ambition",
#        "Palermo",
#        "London",
#        "Scala",
#        "private donations",
#        "nobles",
#        "Venice",
#        "country",
#        "Germany",
#        "musical events",
#        "vaudeville",
#        "Milan",
#        "Hamburg",
#        "contrast",
#        "venues"
#      ]
#transcript = 'An opera house is a theatre building used for opera performances that consists of a stage, an orchestra pit, audience seating, and backstage facilities for costumes and set building.'
#freq_keywords = most_freq_keyword(transcript,keywords)
#
##version 0 = simple, no covariance between keywords and documents. version = 1, covariance is calculated.
#version = 1
#docs = getWikiData(freq_keywords,keywords,version)
##print(docs)

