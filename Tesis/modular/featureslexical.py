#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import nltk
import numpy
import itertools as IT
import ngram
import modular.java as mj

_PATH = 'modular/simmetrics/Example.jar'

def replaceNan(variable):
    result = numpy.isnan(variable)
    if result == False:
        return variable
    else:
        return 0

def get_dice(sentence, sentence1):
    args = [_PATH, sentence, sentence1, '1']
    result = mj.jarWrapper(*args)
    result = [float(x) for x in result]
    for i in result:
        result = i
    result = replaceNan(result)
    return result

def get_euclidean(sentence, sentence1):
    args = [_PATH, sentence, sentence1, '2']
    result = mj.jarWrapper(*args)
    result = [float(x) for x in result]
    for i in result:
        result = i
    result = replaceNan(result)
    return result

def get_jaccard(sentence, sentence1):
    args = [_PATH, sentence, sentence1, '3']
    result = mj.jarWrapper(*args)
    result = [float(x) for x in result]
    for i in result:
        result = i
    result = replaceNan(result)
    return result

def get_jaroWinkler(sentence, sentence1):
    args = [_PATH, sentence, sentence1, '4']
    result = mj.jarWrapper(*args)
    result = [float(x) for x in result]
    for i in result:
        result = i
    result = replaceNan(result)
    return result

def get_levenstein(sentence, sentence1):
    args = [_PATH, sentence, sentence1, '5']
    result = mj.jarWrapper(*args)
    result = [float(x) for x in result]
    for i in result:
        result = i
    result = replaceNan(result)
    return result

def get_overlapCoef(sentence, sentence1):
    args = [_PATH, sentence, sentence1, '6']
    result = mj.jarWrapper(*args)
    result = [float(x) for x in result]
    for i in result:
        result = i
    result = replaceNan(result)
    return result

def get_QGramDistance(sentence, sentence1):
    args = [_PATH, sentence, sentence1, '7']
    result = mj.jarWrapper(*args)
    result = [float(x) for x in result]
    for i in result:
        result = i 
    result = replaceNan(result)
    return result

def get_smithWaterman(sentence, sentence1):
    args = [_PATH, sentence, sentence1, '8']
    result = mj.jarWrapper(*args)
    result = [float(x) for x in result]
    for i in result:
        result = i
    result = replaceNan(result)
    return result

def get_smithWatermanGotoh(sentence, sentence1):
    args = [_PATH, sentence, sentence1, '9']
    result = mj.jarWrapper(*args)
    result = [float(x) for x in result]
    for i in result:
        result = i
    result = replaceNan(result)
    return result

def get_smithWatermanGotohWA(sentence, sentence1):
    args = [_PATH, sentence, sentence1, '10']
    result = mj.jarWrapper(*args)
    result = [float(x) for x in result]
    for i in result:
        result = i
    result = replaceNan(result)
    return result

def get_BlockDistance(sentence, sentence1):
    args = [_PATH, sentence, sentence1, '11']
    result = mj.jarWrapper(*args)
    result = [float(x) for x in result]
    for i in result:
        result = i
    result = replaceNan(result)
    return result

def get_ChapmanLengthDeviation(sentence, sentence1):
    args = [_PATH, sentence, sentence1, '12']
    result = mj.jarWrapper(*args)
    result = [float(x) for x in result]
    result = max(result)
    result = replaceNan(result)
    return result

def get_NedlemanWunch(sentence, sentence1):
    args = [_PATH, sentence, sentence1, '13']
    result = mj.jarWrapper(*args)
    result = [float(x) for x in result]
    result = max(result)
    result = replaceNan(result)
    return result

def get_ChapmanLengthMean(sentence, sentence1):
    args = [_PATH, sentence, sentence1, '14']
    result = mj.jarWrapper(*args)
    result = [float(x) for x in result]
    result = max(result)
    result = replaceNan(result)
    return result

def get_MatchingCoeff(sentence, sentence1):
    args = [_PATH, sentence, sentence1, '15']
    result = mj.jarWrapper(*args)
    result = [float(x) for x in result]
    for i in result:
        result = i
    result = replaceNan(result)
    return result

def get_MongeElkan(sentence, sentence1):
    args = [_PATH, sentence, sentence1, '16']
    result = mj.jarWrapper(*args)
    result = [float(x) for x in result]
    result = max(result)
    result = replaceNan(result)
    return result

def get_Jaro(sentence, sentence1):
    args = [_PATH, sentence, sentence1, '17']
    result = mj.jarWrapper(*args)
    result = [float(x) for x in result]
    for i in result:
        result = i
    result = replaceNan(result)
    return result

def Bigram(list, list1):
    row = 0
    col = 0
    
    row = len(list)
    col = len(list1)

    if col > row:
        matriz = [[0 for j in range(col)] for i in range(col)]
        for i,j in range(col, col):
            matriz[i][j]= 0
    elif row > col:
        matriz = [[0 for j in range(row)] for i in range(row)]
        for i,j in range(row, row):
            matriz[i][j]= 0
    else:
        matriz = [[0 for j in range(col)] for i in range(row)]
    i = 0
    j = 0

    for search, search2 in IT.product(list, list1):

        var = ngram.NGram.compare(search, search2, N=2)

        matriz[i][j] = var
        j+=1

        if j == col and i <= row:
            j=0
            i+=1

       
    return matriz

def Trigram(list, list1):
    row = 0
    col = 0
    
    row = len(list)
    col = len(list1)
    
    if col > row:
        matriz = [[0 for j in range(col)] for i in range(col)]
        for i,j in range(col, col):
            matriz[i][j]= 0
    elif row > col:
        matriz = [[0 for j in range(row)] for i in range(row)]
        for i,j in range(row, row):
            matriz[i][j]= 0
    else:
        matriz = [[0 for j in range(col)] for i in range(row)]
    i = 0
    j = 0

    for search, search2 in IT.product(list, list1):
                
        var = ngram.NGram.compare(search, search2, N=3)

        matriz[i][j] = var
        j+=1

        if j == col and i <= row:
            j=0
            i+=1
       
    return matriz

def Tetragram(list, list1):
    row = 0
    col = 0
    
    row = len(list)
    col = len(list1)

    if col > row:
        matriz = [[0 for j in range(col)] for i in range(col)]
        for i,j in range(col, col):
            matriz[i][j]= 0
    elif row > col:
        matriz = [[0 for j in range(row)] for i in range(row)]
        for i,j in range(row, row):
            matriz[i][j]= 0
    else:
        matriz = [[0 for j in range(col)] for i in range(row)]
    i = 0
    j = 0

    for search, search2 in IT.product(list, list1):
                
        var = ngram.NGram.compare(search, search2, N=4)

        matriz[i][j] = var
        j+=1

        if j == col and i <= row:
            j=0
            i+=1

    return matriz

def SentenceLenghtPhrase(sentence):
    counter = len(sentence)
    return counter
