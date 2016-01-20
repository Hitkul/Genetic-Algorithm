from random import uniform
#import matplotlib.pyplot as plt #Only if Plotting
import operator
import numpy as np

POPULATION_SIZE = 30
LENGTH_OF_BIT_STRING = 32
LOWER_LIMIT = 0
UPPER_LIMIT = 100

def fitness(x):
    #currently set to x^2, later this will be inputted by the user
    return x*x

fitness_list = []
population = []
for j in range(POPULATION_SIZE):
    sample = []
    for i in range(LENGTH_OF_BIT_STRING): #problem with this is that as we increase our bit string sizes, our integers will also increase in value
                                          #Maybe this is because of a small sample set
        if(uniform(0,1)<0.5):
            sample.append('0')#builds a list of strings
        else:
            sample.append('1')
    stringified_sample = ''.join(sample)#converts list of strings into string
    population.append(int(stringified_sample,2))#converts string into binary and adds to our population set
#We now have a population of POPULATION_SIZE
print(population)

#Scale to enter Limits
for i in range(0,POPULATION_SIZE):
    population[i] *= LOWER_LIMIT+((UPPER_LIMIT-LOWER_LIMIT)/float(2**LENGTH_OF_BIT_STRING-1))
    population[i] = int(population[i])
print(population)

#for val in population:
#    val *= LOWER_LIMIT+((UPPER_LIMIT-LOWER_LIMIT)/float(2**LENGTH_OF_BIT_STRING-1))
#    scaled_population.append(int(val))
#    fitness_list.append(fitness(int(val)))

#Here I have my population and fitness in a dictionary for easy access and reference.
#population_and_fitness = dict(zip(scaled_population,fitness_list))

#print(scaled_population)
#print(population_and_fitness)

#matingpool = []
#        -----SELECTION--------
#key, value = max(population_and_fitness.iteritems(), key=lambda x:x[1])
#print(key,value)
#matingpool.append(key)
#del population_and_fitness[key]
#print(population_and_fitness)



#print(population_and_fitness)
#Now our population should be scaled according to our limits
#print(population)
#plt.scatter(range(POPULATION_SIZE),scaled_population)
#plt.scatter(range(POPULATION_SIZE),fitness_list)
#plt.show()
