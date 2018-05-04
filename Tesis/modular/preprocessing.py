#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import nltk
import re
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def clear_tokenize(tokens):
    tokenizer = RegexpTokenizer(r'\w+')
    sentence = tokenizer.tokenize(tokens)
    return sentence

def delete_stop(stop_sentence):
    stop_words = set(stopwords.words("english"))
    filtered_sentence = [w for w in stop_sentence if not w in stop_words]
    return filtered_sentence

def lowercase(lower):

     return lower.lower()
 

def tagger(sen_tag):
    tag = nltk.pos_tag(sen_tag)
    return tag

def tag_stop_word(tag_w, stop_w):
    
    list = []
    for t in tag_w:
            if t[0] in stop_w:
                list.append(t)

    return list

def return_sentence(sentence):
    sentence = " ".join(sentence)
    return sentence

def lemmatizer(stopwords):
    lemmatizer = WordNetLemmatizer()
    lema = [lemmatizer.lemmatize(t) for t in stopwords]
    return lema
    
def syn_lesk(text, stopw, tag):
    
    lemmatzr = WordNetLemmatizer()
    list = []

    for i in tag:

        pos_wn = penn_to_wn(i[1])
        if not pos_wn:
            continue

        lemma = (lemmatzr.lemmatize(i[0]))
        synset = lesk(text, lemma, pos_wn)
        
        if synset is None:
            continue
        else:   
            list.append(synset)

    return list