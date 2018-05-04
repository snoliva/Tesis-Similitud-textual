import arff
import codecs

def readcorpus(filename):
    
    list = []
    openfile = codecs.open(filename, 'r', 'utf-8')
    for line in openfile:
        parts = line.split('\t')
        sentence_1 = parts[0].split(' ',0)
        sentence_2 = parts[1].split(' ', 0)
        list.append(zip(sentence_1,sentence_2))

    return list

def readgs(filename):
    
    with codecs.open(filename) as f:
        list = map(float, f)

    return list 

def recordfile(data, namefile):
    arff.dump(namefile, data, relation="metrics", 
              names=['wup', 'res', 'pathlen', 'lin','lch','jcn','wordsimilarity','dice','euclidean','jaccard','jarwinkler',
                     'levenstein','overlapcoeff','qgram','smithwat','smithwatgot','smithwatgotwinaff',
                     'blockdistance','chapmanlengthdeviation','nedlemanwunch','chapmanlengthmean','matchingcoeff',
                     'mongeelkan','jaro','bigram','trigram','tetragram','staticweigthratio','sentencelenght1','sentencelenght2', 'maxwordsimilarity',
                     'prediction'])