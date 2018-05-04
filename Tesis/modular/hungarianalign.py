import hungarian
import numpy

def alignment(array):
    if len(array) == 0:
        total = 0.0
    else:
        matriz_hung = numpy.array(array)
        vector = hungarian.lap(matriz_hung)[0]
        total = 0
        column = 0
        for row in vector:
            value = array[row][column]
            total += value
            column +=1
    return total

