import random
import math

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
        offsprings
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
    chr_size, pop_size, pc, pm, generation = (8, 100, 0.8, 0.2, 1000)
    population = generatePopulation(pop_size, chr_size)
    for _ in range(generation):
        fit = fitness(population, chr_size)
        newPopulation = []
        elite1, elite2 = elitism(fit)
        newPopulation.append(population[elite1])
        newPopulation.append(population[elite2])
        for _ in range(0, pop_size - 2, 2):
            parentA = RouletteWheel(population, pop_size, fit)
            parentB = RouletteWheel(population, pop_size, fit)
            while(parentA == parentB):
                 parentB = RouletteWheel(population, pop_size, fit)
            offsprings = crossover(parentA[:], parentB[:], pc, chr_size)
            offsprings = mutation(offsprings, pm, chr_size)
            newPopulation.append(offsprings[0])
            newPopulation.append(offsprings[1])
        population = newPopulation
    printNilaiMin(population, chr_size, fit)



def printNilaiMin(population, chr_size, fit):
    idx = fit.index(min(fit))
    decode = decodeChromosome(population[idx], chr_size)

    print("===============Hasil Genetic Algorithm===============")
    print("Kromosom terbaik\t: ", population[idx])
    print("Nilai fitness\t\t: ", fit[idx])
    print("Nilai X\t\t\t: ", decode)
    

generationalReplacement()








# chr_size = 8
# pc = 0.8
# pm = 0.2
# temp = generatePopulation(10, chr_size)
# # temp2 = decodeChromosome(temp[0], 8)
# # print(temp2)
# fit = fitness(temp, chr_size)
# # idx = fit.index(min(fit))

# # print(idx)

# # temp3 = decodeChromosome(temp[idx], 8)

# # print(temp3)
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

# idx = fit.index(min(fit))
# decode = decodeChromosome(temp[idx], chr_size)

# print("===============Hasil Genetic Algorithm===============")
# print("Kromosom terbaik\t: ", temp[idx])
# print("Nilai fitness\t\t: ", fit[idx])
# print("Nilai X\t\t\t: ", decode)