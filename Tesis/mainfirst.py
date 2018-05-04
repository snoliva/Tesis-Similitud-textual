import modular.filefirst as mf
import modular.readfile as rf
import sys
from sys import argv

if __name__ == "__main__":
    array = rf.readcorpus(sys.argv[1])
    if sys.argv[2] == '?':
        score = sys.argv[2]
    else:
        score = rf.readgs(sys.argv[2])
    row = mf.countSpace(array)
    matriz = mf.crearMatriz(row)
    array1 = mf.mandarlista(array,matriz,score)
    rf.recordfile(array1, sys.argv[3])
