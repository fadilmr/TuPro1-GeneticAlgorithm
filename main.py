import random
import math

#initialization
chr_size = 16
pop_size = 5


def generateChromosome(chr_size):
    hasil =[]
        #looping sebanyak chr_size
    for _ in range(chr_size):
        hasil.append(random.randint(0, 1))
    return hasil

def generatePopulation(pop_size, chr_size):
    pop = []
    for i in range(pop_size):
        pop.append(generateChromosome(chr_size))
    return pop

def decodeChromosome(chromosome, chr_size):
    xMin, xMax = (-5, 5)
    yMin, yMax = (-5, 5)

    N, x, y = 0, 0, 0
    n = (chr_size) // 2

    for i in range(0, n):
        N += 2**-(i+1)
    for j in range(0, n):
        x += chromosome[i] * 2 ** -(i+1)
        y += chromosome[n + i] * 2 ** -(i+1)
    x = xMin + (((xMax - xMin) / N) * x) 
    y = yMin + (((yMax - yMin) / N) * y) 
    
    return x, y

def function(x, y):
    return ((math.cos(x)+math.sin(y))**2) / (x**2 + y**2)

def fitness(population):
    hasil = []

    for i in population:
        hasil.append(function(*decodeChromosome(i, 16)))
    return hasil

def tournamentSelection(population, pop_size, tour_size):
    best_chrom = []
    for _ in range(tour_size):
        chrom = population[random.randint(0, pop_size - 1)]
        if (best_chrom == [] or (fitness(best_chrom) < fitness(chrom))):
            best_chrom = chrom
    return best_chrom
    
