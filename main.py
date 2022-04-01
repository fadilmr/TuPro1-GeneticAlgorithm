import random
import math
import time
start_time = time.time()

    # membuat chromosome berdasarkan nilai chr_size
def generateChromosom(chr_size):
    result = []
    for _ in range(chr_size):
        # memasukkan nilai 1 dan 0 secara acak kedalam array result
        result.append(random.randint(0, 1))
    return result

    # membuat population berdasarkan nilai pop_size
def generatePopulation(pop_size, chr_size):
    pop = []
    for _ in range(pop_size):
        # memasukkan chromosome yang sudah dibuat dalam fungsi generateChromosome ke dalam populasi
        pop.append(generateChromosom(chr_size))
    return pop

    # mengubah nilai chromosome menjadi nilai x dan y
def decodeChromosome(chromosome, chr_size):
    # inisialisasi nilai min dan max
    xMin, xMax = (-5, 5)
    yMin, yMax = (-5, 5)

    N, x, y = 0, 0, 0
    n = (chr_size) // 2
    # mendekode nilai chromosome menggunakan cara dekode biner
    for i in range(0, n):
        N += 2**-(i+1)
    for i in range(0, n):
        x += chromosome[i] * 2 ** -(i+1)
        y += chromosome[n + i] * 2 ** -(i+1)
    x = xMin + ((xMax - xMin) / N) * x
    y = yMin + ((yMax - yMin) / N) * y
    
    return [x, y]

    # menghitung nilai dari fungsi 
def Objectivefunction(x, y):
    return ((math.cos(x)+math.sin(y))**2) / (x**2 + y**2)

    # menghitung nilai minimisasi dari fungsi
def function(x, y):
    return 1 / (0.01 + ((math.cos(x)+math.sin(y))**2) / (x**2 + y**2))

    # fungsi untuk memasukkan semua nilai fitness ke dalam array
def fitness(population, chr_size):
    result = []
    for i in population:
        # pemanggilan fungsi function dan decode chromosome
        result.append(function(*decodeChromosome(i, chr_size)))
    return result
    
    # seleksi orang tua metode tournament
def tournament(population, pop_size, tour_size, chr_size):
    result = []
    for _ in range(tour_size):
        # memilih chromosome secara acak
        temp = population[random.randint(0, pop_size - 1)]
        # perbandingan kromosom
        if result == [] or function(decodeChromosome(temp, chr_size)[0], decodeChromosome(temp, chr_size)[0]) < function(decodeChromosome(result, chr_size)[0], decodeChromosome(result, chr_size)[0]):
            result = temp
    return result

    # seleksi orang tua metode Roulette Wheel
def RouletteWheel(population ,pop_size, fitness):
    indv = 0
    # memilih nilai real secara acak
    val = random.uniform(0, 1)
    # menghitung total nilai fitness
    totalfitness = sum(fitness)
    for i in range(pop_size):
        # memilih chromosome secara acak lalu dibandingkan
        if (fitness[i] / totalfitness) > val:
            indv = i
            break
        i += 1
    return population[indv]

    # crossover dengan metode two point crossover
def crossover(parentA, parentB, pc, chr_size):
    # memilih nilai real secara acak
    val = random.uniform(0, 1)
    # jika nilai val lebih kecil dari probabilitas crossover maka akan terjadi crossover
    if val < pc:
        # memilih chromosome secara acak lalu di pindah silangkan
        pindah = random.randint(0, chr_size-1)
        for i in range(pindah):
            parentA[i], parentB[i] = parentB[i], parentA[i]
    return [parentA, parentB]

    # mutasi
def mutation(offsprings, pm, chr_size):
    # memilih nilai real secara acak
    val = random.uniform(0, 1)
    # jika nilai val lebih kecil dari probabilitas mutasi maka akan terjadi mutasi
    if val < pm:
        # mengubah isi kromosom secara acak lalu mengubah nilai nya
        offsprings[0][random.randint(0, chr_size - 1)] = random.randint(0,1) 
        offsprings[1][random.randint(0, chr_size - 1)] = random.randint(0,1) 
    return offsprings

    # menentukan 2 nilai fitness terbaik
def elitism(fit):
    idx1, idx2 = 0, 0
    for i in range(1, len(fit)):
        if fit[i] > fit[idx1]:
            idx2 = idx1
            idx1 = i
    return [idx1, idx2]

def generationalReplacement():
    #initialization
    chr_size, pop_size, pc, pm, generation = (8, 100, 0.8, 0.2, 100)
    tour_size = 5 # Khusus tournamentSelection
    population = generatePopulation(pop_size, chr_size)
    # perulangan sebanyak nilai generation
    for _ in range(generation):
        fit = fitness(population, chr_size)
        newPopulation = []
        elite1, elite2 = elitism(fit)
        newPopulation.append(population[elite1])
        newPopulation.append(population[elite2])
        # menentukan generasi selanjutnya
        for _ in range(0, pop_size - 2, 2):
                    # Menggunakan Tournament Selection
            parentA = tournament(population, pop_size, tour_size, chr_size)
            parentB = tournament(population, pop_size, tour_size, chr_size)
            while(parentA == parentB):
                parentB = tournament(population, pop_size, tour_size, chr_size)  
                    # Menggunakan Roulette Wheel Selection
            # parentA = RouletteWheel(population, pop_size, fit)
            # parentB = RouletteWheel(population, pop_size, fit)
            # while(parentA == parentB):
            #     parentB = RouletteWheel(population, pop_size, fit)
            offsprings = crossover(parentA[:], parentB[:], pc, chr_size)
            offsprings = mutation(offsprings, pm, chr_size)
            newPopulation.extend(offsprings)
    population = newPopulation
    printNilaiMin(population, chr_size, fit)



def printNilaiMin(population, chr_size, fit):
    idx = fit.index(max(fit))
    decode = decodeChromosome(population[idx], chr_size)

    print("===============Hasil Genetic Algorithm===============")
    print("Kromosom terbaik\t: ", population[idx])
    print("Nilai fitness\t\t: ", fit[idx])
    print("Nilai fungsi\t\t: ", Objectivefunction(decode[0], decode[1]))
    print("Nilai X\t\t\t: ", decode[0])
    print("Nilai y\t\t\t: ", decode[1])

    

generationalReplacement()
print("Process finished --- %s seconds ---" % (time.time() - start_time))

# ======================Roulette Wheel Selection======================

# Test dengan chr_size = 8, pop_size = 100, generation = 100:
# ===============Hasil Genetic Algorithm===============
# Kromosom terbaik        :  [1, 1, 0, 1, 1, 0, 0, 1]
# Nilai fitness           :  99.97510572941917
# Nilai fungsi            :  3.9267352965406254e-05
# Nilai X                 :  3.666666666666666
# Nilai y                 :  1.0
# Process finished --- 1.950829267501831 seconds ---

# Test dengan chr_size = 10, pop_size = 150, generation = 200:
# ===============Hasil Genetic Algorithm===============
# Kromosom terbaik        :  [0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
# Nilai fitness           :  99.998222567881
# Nilai fungsi            :  0.013918736270974261
# Nilai X                 :  -5.0
# Nilai y                 :  2.741935483870968
# Process finished --- 17.95911931991577 seconds ---


# =========================Tournament Selection=========================

# Test dengan chr_size = 8, pop_size = 100, tour_size = 4, generation = 100:
# ===============Hasil Genetic Algorithm===============
# Kromosom terbaik        :  [1, 0, 1, 1, 0, 0, 1, 0]
# Nilai fitness           :  99.92237109023498
# Nilai fungsi            :  0.0019007515009992928
# Nilai X                 :  2.333333333333333
# Nilai y                 :  -3.666666666666667
# Process finished --- 0.5887758731842041 seconds ---


# Test dengan chr_size = 10, pop_size = 150, tour_size = 5, generation = 200:
# ===============Hasil Genetic Algorithm===============
# Kromosom terbaik        :  [0, 1, 1, 0, 0, 0, 0, 0, 1, 0]
# Nilai fitness           :  99.93997043687797
# Nilai fungsi            :  0.09196410381771221
# Nilai X                 :  -1.129032258064516
# Nilai y                 :  -4.354838709677419
# Process finished --- 2.4650518894195557 seconds ----