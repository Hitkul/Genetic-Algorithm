from random import randrange,uniform

#import matplotlib.pyplot as plt #Only if Plotting
import numpy as np

POPULATION_SIZE = 31
LENGTH_OF_BIT_STRING = 32
LOWER_LIMIT = 0
UPPER_LIMIT = 100
crossover_probability = 0.5
Mutation_probability = 0.05

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
print("----------------population----------------")
print(pop_fit['chromosome'])

next_gen = []
matingpool=[]

#----SELECTION-----#
next_gen.append(pop_fit[0]['chromosome'])#elitism, to pick the best fitness
pop_fit[0]['flag'] = True
while len(matingpool)<POPULATION_SIZE-1:
    temp = randrange(1,POPULATION_SIZE)
    if(pop_fit[temp]['flag']==False):
        matingpool.append(pop_fit[temp])
        pop_fit[temp]['flag'] = True

#print("----------------mating pool----------------")
#print(matingpool)

#--CROSSOVER THE MATING POOL AND WE GET OUR NEXT GENERATION
for i in range(0,POPULATION_SIZE-1,2):
    for j in range(7):  
        if(uniform(0,1)>crossover_probability):
            if((matingpool[i]['chromosome'] & 2**(6-j))!=(matingpool[i+1]['chromosome'] & 2**(6-j))): #checking for ineqality of bits
                matingpool[i]['chromosome'] = matingpool[i]['chromosome']^2**(6-j) #swapping bits
                matingpool[i+1]['chromosome'] = matingpool[i+1]['chromosome']^2**(6-j) #swapping bits
    next_gen.append(matingpool[i]['chromosome'])
    next_gen.append(matingpool[i+1]['chromosome'])

print("----------------next gen----------------")
print(next_gen)

# -----------------------------MUTATION---------------------------
for i in range(POPULATION_SIZE):
    for j in range(7):
        if(uniform(0,1)<Mutation_probability):
            next_gen[i]=next_gen[i]^2**(6-j)

#remapping into range to correct overflow produced during mutation
for i in range(POPULATION_SIZE):
    next_gen[i] *= LOWER_LIMIT+((UPPER_LIMIT-LOWER_LIMIT)/float(2**7-1))
    next_gen[i] = int(next_gen[i])

next_gen.sort()
next_gen.reverse()
print("----------------next gen after mutation----------------")
print(next_gen)

#TODO terminating condition 


#plt.scatter(range(POPULATION_SIZE),scaled_population)
#plt.scatter(range(POPULATION_SIZE),fitness_list)
#plt.show()