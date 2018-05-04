#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk


def penn_to_wn(tag):
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('N'):
        return wn.NOUN
    elif tag.startswith('R'):
        return wn.ADV
    elif tag.startswith('V'):
        return wn.VERB
    return None

def syn_word(sentence):
    
    lemmatzr = WordNetLemmatizer()
    list = []
    for token in sentence:
        wn_tag = penn_to_wn(token[1])
        
        if not wn_tag:
           continue
       
        lemma = (lemmatzr.lemmatize(token[0], pos=wn_tag))
        synsets = wn.synsets(lemma, pos = wn_tag)
        if not synsets:
            continue
        else:
             
            list.append(wn.synsets(lemma, pos = wn_tag)[0])
    return list

def syn_word_cat(sentence):
    lemmatzr = WordNetLemmatizer()
    list = []
    for token in sentence:
        wn_tag = penn_to_wn(token[1])
        if not wn_tag:
           continue
        lemma = (lemmatzr.lemmatize(token[0], pos=wn_tag))
        list.append(wn.synsets(lemma, pos = wn_tag))
    
    return list

def all_syn(sentence):
    
    lemmatzr = WordNetLemmatizer()
    list = []
    for token in sentence:
        lemma = (lemmatzr.lemmatize(token))
        a = wn.synsets(lemma)
        for t in a:
            list.append(t)

    return list

def syn_les(text, tag):
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