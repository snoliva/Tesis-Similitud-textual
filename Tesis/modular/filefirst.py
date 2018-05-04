#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import arff
import modular.featureslexical as mfet
import modular.hungarianalign as mh
import modular.metrics as mm
import modular.preprocessing as mp
import modular.synsets as ms
from replacers import RegexpReplacer


_NUM = 32
_SPACE = 31

def mandarlista(lista, matriz, list_score): 
    vector = []
    list = matriz   
    replacer = RegexpReplacer()
    
    i = 0
    j = 0

        
    for k in lista:
            for t in k:
            ####################
                lower_1 = mp.lowercase(t[0])
                #print lower_1
                lower_2 = mp.lowercase(t[1])
               # print lower_2
            #''' Expandir frases'''
                #expand_1 = mp.expand_contractions(lower_1)
                expand_1 = replacer.replace(lower_1)
                print expand_1
                #expand_2 = mp.expand_contractions(lower_2)
                expand_2 =  replacer.replace(lower_2)
                print expand_2
            #'''Tokenizar'''
                token_1 = mp.clear_tokenize(expand_1)
            #print token1
                token_2 = mp.clear_tokenize(expand_2)
            #'''TAGGEAR'''
                tag_1 = mp.tagger(token_1)
            #print tag1
                tag_2 = mp.tagger(token_2)
            #'''Borrar stopwords '''
                stop_1 = mp.delete_stop(token_1)
                row = len(stop_1)
            #print stop1
                stop_2 = mp.delete_stop(token_2)
                col = len(stop_2)
            ##########PARA RASGOS LEXICOS##############
                send = mp.return_sentence(stop_1)
                send_1 = mp.return_sentence(stop_2)
            ##########################################    
                
            #print function7
            #'''TAGGEAR LAS PALABRAS '''
                sentence_1 = mp.tag_stop_word(tag_1, stop_1)
                #print sentence1
                sentence_2 = mp.tag_stop_word(tag_2, stop_2)
                
            #'''Synsets frase '''
                synset_1 = ms.syn_word(sentence_1)
                synset_2 = ms.syn_word(sentence_2)
                #synset_cat_1 = syn_word_cat(sentence_1)
                #synset_cat_2 = syn_word_cat(sentence_2)
                
                ################# METRICAS ###################
                if all(not x for x in (synset_1 or synset_2)):
                    total_1 = 0
                    total_2 = 0
                    total_3 = 0
                    total_4 = 0
                    total_5 = 0
                    total_6 = 0
                else:
                    function_1 = mm.sim_wup(synset_1, synset_2)
                    total_1 = mh.alignment(function_1)
                    function_2 = mm.sim_res(synset_1, synset_2)
                    total_2 = mh.alignment(function_2)
                    function_3 = mm.sim_path(synset_1, synset_2)
                    total_3 = mh.alignment(function_3)
                    function_4 = mm.sim_lin(synset_1, synset_2)
                    total_4 = mh.alignment(function_4)
                    #total_4 = [float(x) for x in total_4]
                    #for x in total_4:
                    #    total_4 = x
                        
                    function_5 = mm.sim_lch(synset_1, synset_2)
                    total_5 = mh.alignment(function_5)
                    function_6 = mm.sim_jcn(synset_1, synset_2)
                    total_6 = mh.alignment(function_6)
                ############### MODELS PAPER ####################
                #''' WORD SIMILARITY '''
                #total_29 = mm.word_similarity(synset_1,synset_2)
                total_29 = mm.word_similarity(stop_1, stop_2)
                ####################################
               
                #function_8 = WeiRat(stop_1, synset_cat_2, row, col)
                #total_W1 = alignment(function_8)
                #print total_1
                #function_9 = WeiRat(stop_2, synset_cat_1, col, row)
                #total_W2 = alignment(function_9)
                #print total_2
                #total_19 = (total_W1 + total_W2)/2 
                #print total
                #total_22 = StaticsWeightRatio(total_19)
                
                ############## RASGOS ##################
                
                total_7 = mfet.get_dice(send, send_1)
                #print total_1
                total_8 = mfet.get_euclidean(send, send_1)
                #print total_2
                total_9 = mfet.get_jaccard(send, send_1)
                #print total_3
                total_10 = mfet.get_jaroWinkler(send, send_1)
                #print total_4
                total_11 = mfet.get_levenstein(send, send_1)
                #print total_5
                total_12 = mfet.get_overlapCoef(send, send_1)
                #print total_6
                total_13 = mfet.get_QGramDistance(send, send_1)
                #print total_7
                total_14 = mfet.get_smithWaterman(send, send_1)
                #print total_8
                total_15 = mfet.get_smithWatermanGotoh(send, send_1)
                #print total_9
                total_16 = mfet.get_smithWatermanGotohWA(send, send_1)
                
                total_17 = mfet.get_BlockDistance(send, send_1)
                #print total_17
                total_18 = mfet.get_ChapmanLengthDeviation(send, send_1)
                #print total_18
                total_19 = mfet.get_NedlemanWunch(send, send_1)
                #print total_19
                total_20 = mfet.get_ChapmanLengthMean(send, send_1)
                #print total_20
                total_21 = mfet.get_MatchingCoeff(send, send_1)
                #print total_21
                #print total_10
                total_22 = mfet.Bigram(stop_1, stop_2)
                total_22 = mh.alignment(total_22)
                #print total_11
                total_23 = mfet.Trigram(stop_1, stop_2)
                total_23 = mh.alignment(total_23)
                #print total_12
                total_24 = mfet.Tetragram(stop_1, stop_2)
                total_24 = mh.alignment(total_24)
                
                 ########## staticweightratio
                hal = mm.hal(stop_1, stop_2)
                #print hal
                function25= mm.StaticsWeightRatio(stop_1, stop_2, hal)
                total_25 = mh.alignment(function25)
                #total_19 = WeiRat(stop_1, synset_2, row, col)
                #total_19 = alignment(total_19)
                
                total_26 = mfet.SentenceLenghtPhrase(stop_1)
                total_27 = mfet.SentenceLenghtPhrase(stop_2)
                
                total_28 = mm.MaxWordSimilarity(stop_1, stop_2, synset_1, synset_2, hal)
                
                total_30 = mfet.get_MongeElkan(send, send_1)
                
                total_31 = mfet.get_Jaro(send, send_1)
                #print stop2
                #print total_16
                #print total_13
                '''if all(not x for x in (synset1 or synset2)):
                    total1 = 0
                    total2 = 0
                    total3 = 0
                    total4 = 0
                    total5 = 0
                    total6 = 0
                else:
                    function1 = sim_wup(synset1, synset2)
                    total1 = alignment(function1)
                    function2 = sim_res(synset1, synset2)
                    total2 = alignment(function2)
                    function3 = sim_path(synset1, synset2)
                    total3 = alignment(function3)
                    function4 = sim_lin(synset1, synset2)
                    total4 = alignment(function4)
                    function5 = sim_lch(synset1, synset2)
                    total5 = alignment(function5)
                    function6 = sim_jcn(synset1, synset2)
                    total6 = alignment(function6)'''
            #'''llenar vector'''
                vector.append(total_1)
                vector.append(total_2)
                vector.append(total_3)
                vector.append(total_4)
                vector.append(total_5)
                vector.append(total_6)
                vector.append(total_29)
                #for num in function_7:
                #    vector.append(num)
                vector.append(total_7)
                vector.append(total_8)
                vector.append(total_9)
                vector.append(total_10)
                vector.append(total_11)
                vector.append(total_12)
                vector.append(total_13)
                vector.append(total_14)
                vector.append(total_15)
                vector.append(total_16)
                vector.append(total_17)
                vector.append(total_18)
                vector.append(total_19)
                vector.append(total_20)
                vector.append(total_21)
                
                vector.append(total_30)
                vector.append(total_31)
                
                vector.append(total_22)
                vector.append(total_23)
                vector.append(total_24)
                vector.append(total_25)
                vector.append(total_26)
                vector.append(total_27)
                vector.append(total_28)
                
                
                
            #''' For function word similarity'''
                #for num in function7:
                #    vector.append(num)
            #list.append(vector)
                #for numbers in vector:
                #print numbers
                #    list[i][j] = numbers
                #    j+=1
                
            #list.insert(position, vector)
                #function1 = WeiRat(stop1, synset2, row, col)
                #total1 = alignment(function1)
                #vector.append(total1)
                for numbers in vector:
                #print numbers
                    list[i][j] = numbers
                    j+=1
                i+=1
                j = 0
            print i
            
            #position +=1
            #print list
            del vector[:]
    x = 0
    if list_score == '?':
        while x < i:
            list[x][_SPACE] = list_score
            x +=1
    else:
         i = 0
         for x in list_score:
        #result = [float(y) for y in x] 
        #for k in result:
        #    result = k
            list[i][_SPACE] = x
            i+=1  
       #     break   
    #print list
    return list



def countSpace(list):
    count = len(list)

    return count
def crearMatriz(row):
    col = _NUM #_NUM Definimos número de columnas (numero de metricas)
    matriz = [[0 for j in range(col)] for i in range(row)]
    return matriz
