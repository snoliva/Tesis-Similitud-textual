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
                
                lower_1 = mp.lowercase(t[0])
                lower_2 = mp.lowercase(t[1])

                expand_1 = replacer.replace(lower_1)
                print expand_1
                expand_2 =  replacer.replace(lower_2)
                print expand_2

                token_1 = mp.clear_tokenize(expand_1)
                token_2 = mp.clear_tokenize(expand_2)

                tag_1 = mp.tagger(token_1)
                tag_2 = mp.tagger(token_2)

                stop_1 = mp.delete_stop(token_1)
                row = len(stop_1)

                stop_2 = mp.delete_stop(token_2)
                col = len(stop_2)

                send = mp.return_sentence(stop_1)
                send_1 = mp.return_sentence(stop_2)

                sentence_1 = mp.tag_stop_word(tag_1, stop_1)
                sentence_2 = mp.tag_stop_word(tag_2, stop_2)
                
                sen1 = mp.return_sentence(token_1)
                sen2 = mp.return_sentence(token_2)
                
                synset_1 = ms.syn_les(sen1, sentence_1)
                synset_2 = ms.syn_les(sen2, sentence_2)

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
                    function_5 = mm.sim_lch(synset_1, synset_2)
                    total_5 = mh.alignment(function_5)
                    function_6 = mm.sim_jcn(synset_1, synset_2)
                    total_6 = mh.alignment(function_6)
 
                total_29 = mm.word_similarity(stop_1, stop_2)
                
                total_7 = mfet.get_dice(send, send_1)
              
                total_8 = mfet.get_euclidean(send, send_1)
               
                total_9 = mfet.get_jaccard(send, send_1)
                
                total_10 = mfet.get_jaroWinkler(send, send_1)
               
                total_11 = mfet.get_levenstein(send, send_1)
             
                total_12 = mfet.get_overlapCoef(send, send_1)
               
                total_13 = mfet.get_QGramDistance(send, send_1)
                
                total_14 = mfet.get_smithWaterman(send, send_1)
               
                total_15 = mfet.get_smithWatermanGotoh(send, send_1)
            
                total_16 = mfet.get_smithWatermanGotohWA(send, send_1)
                
                total_17 = mfet.get_BlockDistance(send, send_1)
             
                total_18 = mfet.get_ChapmanLengthDeviation(send, send_1)

                total_19 = mfet.get_NedlemanWunch(send, send_1)

                total_20 = mfet.get_ChapmanLengthMean(send, send_1)

                total_21 = mfet.get_MatchingCoeff(send, send_1)

                total_22 = mfet.Bigram(stop_1, stop_2)
                total_22 = mh.alignment(total_22)

                total_23 = mfet.Trigram(stop_1, stop_2)
                total_23 = mh.alignment(total_23)
   
                total_24 = mfet.Tetragram(stop_1, stop_2)
                total_24 = mh.alignment(total_24)
                
                hal = mm.hal(stop_1, stop_2)
                function25= mm.StaticsWeightRatio(stop_1, stop_2, hal)
                total_25 = mh.alignment(function25)

                
                total_26 = mfet.SentenceLenghtPhrase(stop_1)
                total_27 = mfet.SentenceLenghtPhrase(stop_2)
                
                total_28 = mm.MaxWordSimilarity(stop_1, stop_2, synset_1, synset_2, hal)
                
                total_30 = mfet.get_MongeElkan(send, send_1)
                total_31 = mfet.get_Jaro(send, send_1)

                vector.append(total_1)
                vector.append(total_2)
                vector.append(total_3)
                vector.append(total_4)
                vector.append(total_5)
                vector.append(total_6)
                vector.append(total_29)
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

                for numbers in vector:
                    list[i][j] = numbers
                    j+=1
                i+=1
                j = 0
            print i
            del vector[:]
    x = 0
    if list_score == '?':
        while x < i:
            list[x][_SPACE] = list_score
            x +=1
    else:
         i = 0
         for x in list_score:
            list[i][_SPACE] = x
            i+=1 

    return list



def countSpace(list):
    count = len(list)
    return count

def crearMatriz(row):
    col = _NUM 
    matriz = [[0 for j in range(col)] for i in range(row)]
    return matriz