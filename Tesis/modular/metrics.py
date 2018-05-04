#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import nltk
import math
import itertools as IT
import modular.synsets as ms
import modular.preprocessing as mp
import modular.java as mj
import modular.hungarianalign as mh
import modular.featureslexical as mfet

from nltk.stem import WordNetLemmatizer
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from collections import Counter

brown_ic = wordnet_ic.ic('ic-brown.dat')
semcor_ic = wordnet_ic.ic('ic-semcor.dat')

_PATH = 'modular/hal/HAL.jar'

def replaceNone(variable):
    if variable is None:
        return 0
    else:
        return variable
    

def sim_path(list, list1):
    
    lista = []
    lista1 = []
    row = 0
    col = 0
    
    for t in list:
        lista.append(t.name())
        row +=1 
    for y in list1:
        lista1.append(y.name())
        col +=1
    
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

    for x, z in IT.product(lista, lista1):
        
        var = wn.synset(x).path_similarity(wn.synset(z))
        result = replaceNone(var)
        matriz[i][j] = result
        j+=1
        if j == col and i <= row:
            j = 0
            i+=1
    
    return matriz

def sim_wup(list, list1):
    
    lista = []
    lista1 = []
    row = 0
    col = 0
    
    for t in list:
        lista.append(t.name())
        row +=1 
    for y in list1:
        lista1.append(y.name())
        col +=1
    
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
    for x, z in IT.product(lista, lista1):
        
        var = wn.synset(x).wup_similarity(wn.synset(z))
        result = replaceNone(var)
        matriz[i][j] = result
        j+=1
        if j == col and i <= row:
            j = 0
            i+=1
       
    return matriz

def sim_lch(list, list1):
    
    lista = []
    lista1 = []
    row = 0
    col = 0
    
    for t in list:
        lista.append(t.name())
        row +=1 
    for y in list1:
        lista1.append(y.name())
        col +=1
    
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
          
            if search.pos() == search2.pos():
                
                var = wn.synset(lista[i]).lch_similarity(wn.synset(lista1[j]))
                
                result = replaceNone(var)
                matriz[i][j] = result
                j+=1
                
            
            else:
                
                matriz[i][j] = -1
                j+=1
                
            if j == col and i <= row:
                j=0
                i+=1
    
    return matriz

def sim_res(list, list1):
    
    lista = []
    lista1 = []
    row = 0
    col = 0
    
    for t in list:
        lista.append(t.name())
        row +=1 
    for y in list1:
        lista1.append(y.name())
        col +=1
    
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
          
        if search.pos() == search2.pos() and all(x != 'a' for x in (search.pos(),search2.pos())) and all(y != 's' for y in (search.pos(),search2.pos())) and all(z != 'r' for z in (search.pos(),search2.pos())):   
            var = wn.synset(lista[i]).res_similarity(wn.synset(lista1[j]), brown_ic)
                
            result = replaceNone(var)
            matriz[i][j] = result
            j+=1
                
            
        else:
                
            matriz[i][j] = -1
            j+=1
                
        if j == col and i <= row:
            j=0
            i+=1

    return matriz

def sim_jcn(list, list1):
    lista = []
    lista1 = []
    row = 0
    col = 0
    
    for t in list:
        lista.append(t.name())
        row +=1 
    for y in list1:
        lista1.append(y.name())
        col +=1
    
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
          
        if search.pos() == search2.pos() and all(x != 'a' for x in (search.pos(),search2.pos())) and all(y != 's' for y in (search.pos(),search2.pos())) and all(z != 'r' for z in (search.pos(),search2.pos())):
                
            var = wn.synset(lista[i]).jcn_similarity(wn.synset(lista1[j]), brown_ic)
                
            result = replaceNone(var)
            matriz[i][j] = result
            j+=1
                
        else:
                
            matriz[i][j] = 0
            j+=1
                
        if j == col and i <= row:
            j=0
            i+=1

    return matriz

def sim_lin(list, list1):
    lista = []
    lista1 = []
    row = 0
    col = 0
    
    for t in list:
        lista.append(t.name())
        row +=1 
    for y in list1:
        lista1.append(y.name())
        col +=1
        
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
          
        if search.pos() == search2.pos() and all(x != 'a' for x in (search.pos(),search2.pos())) and all(y != 's' for y in (search.pos(),search2.pos())) and all(z != 'r' for z in (search.pos(),search2.pos())):
                
            var = wn.synset(lista[i]).lin_similarity(wn.synset(lista1[j]), semcor_ic)
                
            result = replaceNone(var)
            matriz[i][j] = result
            j+=1
                
        else:
                
            matriz[i][j] = 0
            j+=1
                
        if j == col and i <= row:
            j=0
            i+=1
    return matriz  

def word_similarity(stopw, stopw1):
    
    array = []
    array_1 = []
 
    row = len(stopw)
    col = len(stopw1)

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
    
    x = 0    
    y = 0

    for k, z in IT.product(stopw, stopw1):
         
        list = ms.all_syn(k)
        list1 = ms.all_syn(z)
        
        if all(not x for x in (list, list1)):
            array = [0,0,0,0,0,0]
        else:

            path_len = sim_path(list, list1) 
            for i in path_len:
                for j in i:
                    array_1.append(j)
            
            max_valor = max(array_1)
            array.append(max_valor)
            del array_1[:]
    
            wup = sim_wup(list, list1)
            for i in wup:
                for j in i:
                    array_1.append(j)
            
            max_valor = max(array_1)
            array.append(max_valor)
            del array_1[:]
    
            lch = sim_lch(list, list1)
            for i in lch:
                for j in i:
                    array_1.append(j)
            
            max_valor = max(array_1)
            array.append(max_valor)
            del array_1[:]
    
            res = sim_res(list, list1)
            for i in res:
                for j in i:
                    array_1.append(j)
            
            max_valor = max(array_1)
            array.append(max_valor)
            del array_1[:]
    
            jcn = sim_jcn(list, list1)
            for i in jcn:
                for j in i:
                    array_1.append(j)
            
            max_valor = max(array_1)
            array.append(max_valor)
            del array_1[:]
    
            lin = sim_lin(list, list1)
            for i in lin:
                for j in i:
                    array_1.append(j)
            
            max_valor = max(array_1)
            array.append(max_valor)
            del array_1[:]

            array = [l for l in array if l != 1e+300] 
            if not array:
                result = 0
            else:               
                result = max(array)
            del array[:]
            matriz[x][y] = result
            y+=1

            if y == col and x <= row:
                y=0
                x+=1
           
        score = mh.alignment(matriz)
    return score     




def WeiRat(word1, word2):
    
    array = []
    array_1 = []
    list_syn = []
    list_name = []

    synset1 = ms.all_syn([word2])

    conteo = 0       
    a = 0
    b = 0 
    k = 0

    list_antonym = []
    list_hypernym = []
    list_hyponym = []
    list_gloss = []

    while conteo == 0:
        
        if not synset1:
            conteo = 9
       
        for i in synset1:
                k +=1
                names = i.lemmas()[0].antonyms()      
                gloss = i.definition()
                list_gloss.append(mp.clear_tokenize(gloss))
                hyper = i.hypernyms()
                hypon = i.hyponyms()
            
                for x in hyper:
                    list_hypernym.append(x.lemma_names()[0])
                for x in hypon:
                    list_hyponym.append(x.lemma_names()[0])
                for x in names:
                    list_antonym.append(x.name())
                for j in i.lemmas():
                    list_syn.append(j.name())

        if word1 in list_syn:
            conteo = 1

        if word1 in list_antonym:
            conteo = 10
    
        if word1 in list_hypernym:
            conteo = 2
   
        if word1 in list_hyponym:
            conteo = 3

        count = 0
        for gloss in list_gloss:
            total = len(gloss)
            for match in gloss:
                if word1 == match:
                    count +=1
                else: 
                    continue 
                       
            if count >= total/2:
                conteo = 3

        if conteo == 0:
           conteo = 9

      
    return conteo

def StaticsWeightRatio(stopw, stopw1, matrizHal):
    list = []
    list1 = []
    row = len(stopw)
    col = len(stopw1)
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

    for w1, w2 in IT.product(stopw, stopw1):

        args2 = WeiRat(w1, w2)
        simHal = matrizHal[i][j] 
        staWeiRat = (simHal + float(1)/args2)/2
        
        matriz[i][j] = staWeiRat
        j+=1    
        if j == col and i <= row:
            j=0
            i+=1
    return matriz

def MaxWordSimilarity(stopw, stopw1, synset, synset1, hal):
    
    list = []
    list1 = []
    array = sim_wup(synset, synset1) 

    row = len(stopw)
    col = len(stopw1)
    
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

    lensyn1 = len(synset)
    lensyn2 = len(synset1) 
    i = 0
    j = 0
    valor = 0 
    
    for search, search2 in IT.product(stopw, stopw1):

        result = mfet.get_QGramDistance(search, search2)
        
        if result == 1:
           matriz[i][j] = result
           j+=1
        else:
            simHal = hal[i][j] 
            
            if j >= lensyn2 or i >= lensyn1: 
                valor = 0
            else:
                valor = array[i][j]
   
            max_valor = max(simHal, valor) 
            matriz[i][j] = max_valor
            j+=1

        if j == col and i <= row:
            j=0
            i+=1
            
    total = mh.alignment(matriz)
    return total

def hal(stopw, stopw1):
    
    row = len(stopw)
    col = len(stopw1)
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
   
    for w1, w2 in IT.product(stopw, stopw1):
  
        args = [_PATH, w1, w2]
        result = mj.jarWrapper(*args)
        result = [float(x) for x in result] 
        #print result
        for x in result:
            simHal = x
        matriz[i][j] = simHal
        j+=1
        if j == col and i <= row:
            j=0
            i+=1
            
    return matriz  
