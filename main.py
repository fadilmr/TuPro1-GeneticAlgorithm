import random
import math

#initialization
chr_size = 8
pop_size = 8
pc = 0.8
pm = 0.2

def generateChromosom(chr_size):
    result = []
    for _ in range(chr_size):
        result.append(random.randint(0, 1))
    return result

def generatePopulation(pop_size, chr_size):
    pop = []
    for _ in range(pop_size):
        pop.append(generateChromosom(chr_size))
    return pop

def decodeChromosome(chromosome, chr_size):
    xMin, xMax = (-5, 5)
    yMin, yMax = (-5, 5)

    N, x, y = 0, 0, 0
    n = (chr_size) // 2

    for i in range(0, n):
        N += 2**-(i+1)
    for i in range(0, n):
        x += chromosome[i] * 2 ** -(i+1)
        y += chromosome[n + i] * 2 ** -(i+1)
    x *= (xMax - xMin / N)
    y *= (yMax - yMin / N)
    x += xMin
    y += yMin
    
    return [x, y]

def function(x, y):
    return ((math.cos(x)+math.sin(y))**2) / (x**2 + y**2)

def fitness(population, chr_size):
    result = []
    for i in population:
        result.append(function(*decodeChromosome(i, chr_size)))
    return result
    
def RouletteWheel(populasi ,pop_size, fitness):
    indv = 0
    val = random.uniform(0, 1)
    totalfitness = sum(fitness)
    for i in range(pop_size):
        if (fitness[i] / totalfitness) > val:
            indv = i
        i += 1
    return populasi[indv]

def crossover(parentA, parentB, pc, chr_size):
    val = random.uniform(0, 1)
    if val < pc:
        pindah = random.randint(0, chr_size-1)
        for i in range(pindah):
            parentA[i], parentB[i] = parentB[i], parentA[i]
    return [parentA, parentB]

def mutation(offsprings, pm, chr_size):
    val = random.uniform(0, 1)
    if val < pm:
        offsprings[0][random.randint(0, chr_size - 1)] = random.randint(0,1) 
        offsprings[1][random.randint(0, chr_size - 1)] = random.randint(0,1) 
        offsprings
    return offsprings

def elitism(fitness):
    fitness.sort()
    idx1 = fitness[0]
    idx2 = fitness[1]
    return [idx1, idx2]


# temp = generatePopulation(pop_size, chr_size)
# fit = fitness(temp, chr_size)
# p1 = RouletteWheel(temp, chr_size, fit)
# p2 = RouletteWheel(temp, chr_size, fit)
# while (p1 == p2) :
#     p2 = RouletteWheel(temp, chr_size, fit)
# offsprings = crossover(p1[:], p2[:], pc, chr_size)

# print (temp)
# print ("------------------------------------------------------")

# print (p1)
# print (p2)

# print ("------------------------------------------------------")

# print(offsprings)

# print ("------------------------------------------------------")

# mutasi = mutation(offsprings, pm, chr_size)
# print(mutasi)

# print ("------------------------------------------------------")

# elit = elitism(fit)
# print(elit)