import random
import math


def generateChromosome(chr_size):
    hasil =[]

        #looping sebanyak chr_size
    for _ in range(chr_size):
        hasil.append(random.randint(0, 1))
    return  hasil

def decodeChromosome(chromosome, chr_size):
    xMin, xMax = (-5, 5)
    yMin, yMax = (-5, 5)

    N, x, y = 0, 0, 0
    n = (chr_size) // 2

    for i in range(0, n):
        N += 2**-(i+1)
    for j in range(0, n):
        x += chromosome[i] * 2 ** -(i+1)
        x += chromosome[n + i] * 2 ** -(i+1)
    x = xMin + (((xMax - xMin) / N) * x) 
    y = yMin + (((yMax - yMin) / N) * y) 
        
    return [x, y]




