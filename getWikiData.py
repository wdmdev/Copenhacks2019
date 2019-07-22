
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
            keywords[i] = ps.stem(keyword)
        
    for i, word in enumerate(words):
        if word in keywords:
           tempArr[word] = count[i]
            
            
    temp = np.sort(list(tempArr.values()))[::-1]
    
    
    
    new_keywords = []
    if len(tempArr) < 3:
        n = len(tempArr)
    else:
        n = 3

    for keyphrase, value in tempArr.items():
        if value in temp[:n]:
            new_keywords.append(keyphrase)

    return dict(zip(new_keywords, temp[:n]))