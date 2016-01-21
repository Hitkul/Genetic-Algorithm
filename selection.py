from random import randrange,uniform

#import matplotlib.pyplot as plt #Only if Plotting
import numpy as np

POPULATION_SIZE = 31
LENGTH_OF_BIT_STRING = 32
LOWER_LIMIT = 0
UPPER_LIMIT = 100

#TODO MODULARIZE EVERYTHING
def fitness(x):
    #currently set to x^2, later this will be inputted by the user
    return x*x

population = []
for j in range(POPULATION_SIZE):
    sample = []
    for i in range(LENGTH_OF_BIT_STRING):
        if(uniform(0,1)<0.5):
            sample.append('0')#builds a list of strings
        else:
            sample.append('1')
    stringified_sample = ''.join(sample)#converts list of strings into string
    population.append(int(stringified_sample,2))#converts string into binary and adds to our population set
#We now have a population of POPULATION_SIZE
#print(population)
type = [('chromosome',int), ('fitness',int),('flag',bool)]
pop_fit = np.zeros((POPULATION_SIZE,),dtype = type)#Create a structured 1D array to store population and fitness

#Scale to enter Limits
for i in range(0,POPULATION_SIZE):
    population[i] *= LOWER_LIMIT+((UPPER_LIMIT-LOWER_LIMIT)/float(2**LENGTH_OF_BIT_STRING-1))
    population[i] = int(population[i])
    pop_fit[i] = (population[i],fitness(population[i]),False)
pop_fit = np.sort(pop_fit,order='fitness')[::-1]
print(pop_fit)

next_gen = []
matingpool=[]

#----SELECTION-----#
next_gen.append(pop_fit[0])#elitism, to pick the best fitness
pop_fit[0]['flag'] = True
while len(matingpool)<POPULATION_SIZE-2:
    temp = randrange(1,POPULATION_SIZE-1)
    if(pop_fit[temp]['flag']==False):
        matingpool.append(pop_fit[temp])
        pop_fit[temp]['flag'] = True
#TODO MAKE MATING POOL IN PLACE SO THAT WE USE LESS MEMORY PER GENERATION

print(matingpool)
#--CROSSOVER THE MATING POOL AND WE GET OUR NEXT GENERATION





#plt.scatter(range(POPULATION_SIZE),scaled_population)
#plt.scatter(range(POPULATION_SIZE),fitness_list)
#plt.show()
