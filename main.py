import random
import math

class GA:
    def __init__(self):
        pass

    def generateChromosome(self):
        hasil =[]
            #looping sebanyak chr_size
        for _ in range(self):
            hasil.append(random.randint(0, 1))
        return  hasil

    def decodeChromosome(self):
        xMin, xMax = (-5, 5)
        yMin, yMax = (-5, 5)

        N, x, y = 0, 0, 0
        n = (self) // 2

        for i in range(0, n):
            N += 2**-(i+1)
        for j in range(0, n):
            x += self[i] * 2 ** -(i+1)
            y += self[n + i] * 2 ** -(i+1)
        x = xMin + (((xMax - xMin) / N) * x) 
        y = yMin + (((yMax - yMin) / N) * y) 
            
        return [x, y]

    def fungsi(self):
         return ((math.cos(self)+math.sin(self))**2) / (self**2 + self**2)

    def fitness(self):
        hasil = []
         
        for i in self:
            hasil.append(self)
        pass

    def touramentSelection(self):
        pass
    
    def crosover(self):
        pass

    def mutasi(self):
        pass

    def seleksiSurvivor(self):
        pass

    def perpindahanGenerasi(self):
        pass

    def printGA():
        pass



