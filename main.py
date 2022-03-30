import random
import math
import time
start_time = time.time()

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
    x = xMin + ((xMax - xMin) / N) * x
    y = yMin + ((yMax - yMin) / N) * y
    
    return [x, y]

def function(x, y):
    return ((math.cos(x)+math.sin(y))**2) / (x**2 + y**2)

def fitness(population, chr_size):
    result = []
    for i in population:
        result.append(function(*decodeChromosome(i, chr_size)))
    return result
    
def tournament(population, pop_size, tour_size, chr_size):
    result = []
    for _ in range(tour_size):
        temp = population[random.randint(0, pop_size - 1)]
        if result == [] or function(decodeChromosome(temp, chr_size)[0], decodeChromosome(temp, chr_size)[0]) > function(decodeChromosome(result, chr_size)[0], decodeChromosome(result, chr_size)[0]):
            result = temp
    return result

def RouletteWheel(population ,pop_size, fitness):
    indv = 0
    val = random.uniform(0, 1)
    totalfitness = sum(fitness)
    for i in range(pop_size):
        if (fitness[i] / totalfitness) > val:
            indv = i
            break
        i += 1
    return population[indv]

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
    return offsprings

def elitism(fit):
    idx1, idx2 = 0, 0
    for i in range(1, len(fit)):
        if fit[i] < fit[idx1]:
            idx2 = idx1
            idx1 = i
    return [idx1, idx2]

def generationalReplacement():
    #initialization
    chr_size, pop_size, pc, pm, generation = (16, 150, 0.8, 0.2, 1000)
    tour_size = 5 # Khusus tournamentSelection
    population = generatePopulation(pop_size, chr_size)
    for _ in range(generation):
        fit = fitness(population, chr_size)
        newPopulation = []
        elite1, elite2 = elitism(fit)
        newPopulation.append(population[elite1])
        newPopulation.append(population[elite2])
        for _ in range(0, pop_size - 2, 2):
                    # Menggunakan Tournament Selection
            # parentA = tournament(population, pop_size, tour_size, chr_size)
            # parentB = tournament(population, pop_size, tour_size, chr_size)
            # while(parentA == parentB):
            #     parentB = tournament(population, pop_size, tour_size, chr_size)  
                    # Menggunakan Roulette Wheel Selection
            parentA = RouletteWheel(population, pop_size, fit)
            parentB = RouletteWheel(population, pop_size, fit)
            while(parentA == parentB):
                parentB = RouletteWheel(population, pop_size, fit)
            offsprings = crossover(parentA[:], parentB[:], pc, chr_size)
            offsprings = mutation(offsprings, pm, chr_size)
            newPopulation.extend(offsprings)
    population = newPopulation
    printNilaiMin(population, chr_size, fit)



def printNilaiMin(population, chr_size, fit):
    idx = fit.index(min(fit))
    decode = decodeChromosome(population[idx], chr_size)

    print("===============Hasil Genetic Algorithm===============")
    print("Kromosom terbaik\t: ", population[idx])
    print("Nilai fitness\t\t: ", fit[idx])
    print("Nilai X\t\t\t: ", decode[0])
    print("Nilai y\t\t\t: ", decode[1])

    

generationalReplacement()
print("Process finished --- %s seconds ---" % (time.time() - start_time))

# ======================Roulette Wheel Selection======================

# Test dengan chr_size = 8, pop_size = 100:
# ===============Hasil Genetic Algorithm===============
# Kromosom terbaik        :  [0, 1, 1, 1, 1, 0, 1, 1]
# Nilai fitness           :  1.3455611681304287e-05
# Nilai X                 :  -0.3333333333333339
# Nilai y                 :  2.333333333333333
# Process finished --- 1.494236707687378 seconds ---


# Test dengan chr_size = 16, pop_size = 150:
# ===============Hasil Genetic Algorithm===============
# Kromosom terbaik        :  [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0]
# Nilai fitness           :  1.1010545647825181e-06
# Nilai X                 :  -4.529411764705882
# Nilai y                 :  -1.3137254901960786
# Process finished --- 3.4147183895111084 seconds ---
#=======================================================================


# =========================Tournament Selection=========================

# Test dengan chr_size = 8, pop_size = 100, tour_size = 4:
# ===============Hasil Genetic Algorithm===============
# Kromosom terbaik        :  [1, 0, 0, 1, 1, 0, 1, 0]
# Nilai fitness           :  3.926735296540477e-05
# Nilai X                 :  1.0
# Nilai y                 :  1.666666666666666
# Process finished --- 6.051281213760376 seconds ---


# Test dengan chr_size = 16, pop_size = 150, tour_size = 5:
# ===============Hasil Genetic Algorithm===============
# Kromosom terbaik        :  [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1]
# Nilai fitness           :  1.3917991868080088e-06
# Nilai X                 :  -1.6274509803921569
# Nilai y                 :  -4.7254901960784315
# Process finished --- 17.66501498222351 seconds ---