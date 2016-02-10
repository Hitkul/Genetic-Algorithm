from random import randrange,uniform
#import matplotlib.pyplot as plt    #Only if Plotting
import numpy as np

#~~~~~~~~~~~~~~~~~~~~~~functions~~~~~~~~~~~~~~~~~~~~
def fitness(x):
    #currently set to x^2, later this will be inputted by the user
    return x*x

def population_generation():
    for j in range(POPULATION_SIZE):
        sample = []
        for i in range(LENGTH_OF_BIT_STRING):
            if(uniform(0,1)<0.5):
                sample.append('0')#builds a list of strings
            else:
                sample.append('1')
        stringified_sample = ''.join(sample)#converts list of strings into string
        population.append(int(stringified_sample,2))#converts string into binary and adds to our population set


def scale(start_point,UPPER_LIMIT,LOWER_LIMIT,POPULATION_SIZE,LENGTH_OF_BIT_STRING,population):
    for i in range(start_point,POPULATION_SIZE):
        population[i] *= LOWER_LIMIT+((UPPER_LIMIT-LOWER_LIMIT)/float(2**LENGTH_OF_BIT_STRING-1))
        population[i] = int(population[i])


def get_fitness():
    for i in range(0,POPULATION_SIZE):        
        pop_fit[i] = (population[i],fitness(population[i]),False)
    


def selection():
    while len(matingpool)<POPULATION_SIZE-1:
        temp = randrange(1,POPULATION_SIZE)
        if(pop_fit[temp]['flag']==False):
            matingpool.append(pop_fit[temp]['chromosome'])
            pop_fit[temp]['flag'] = True


def crossover():
    for i in range(0,POPULATION_SIZE-1,2):
        for j in range(7):  
            if(uniform(0,1)>crossover_probability):
                if((matingpool[i] & 2**(6-j))!=(matingpool[i+1] & 2**(6-j))): #checking for inequality of bits
                    matingpool[i] = matingpool[i]^2**(6-j) #swapping bits
                    matingpool[i+1] = matingpool[i+1]^2**(6-j) #swapping bits
        next_gen.append(matingpool[i])
        next_gen.append(matingpool[i+1])


def mutation():
    for i in range(1,POPULATION_SIZE):
        for j in range(7):
            if(uniform(0,1)<Mutation_probability):
                next_gen[i]=next_gen[i]^2**(6-j)


#~~~~~~~~~~~~~~~~~~~~~constant values~~~~~~~~~~~~~~~~~
POPULATION_SIZE = 31
LENGTH_OF_BIT_STRING = 32
LOWER_LIMIT = 0
UPPER_LIMIT = 100
crossover_probability = 0.5
Mutation_probability = 0.01
next_gen = []
matingpool=[]
no_of_generations =100
population = []
count =0
type = [('chromosome',int), ('fitness',int),('flag',bool)]


#~~~~~~~~~~~~~~~~~~~~MAIN~~~~~~~~~~~~~~~~~~~~~~~~~

population_generation()

#We now have a initial population of POPULATION_SIZE

#Scale population into Limits
scale(0,UPPER_LIMIT,LOWER_LIMIT,POPULATION_SIZE,LENGTH_OF_BIT_STRING,population)

pop_fit = np.zeros((POPULATION_SIZE,),dtype = type)#Create a structured 1D array to store population and fitness
get_fitness()   #get fitness of chromosomes
pop_fit = np.sort(pop_fit,order='fitness')[::-1]

print '------------------------------initial population----------------'
print pop_fit['chromosome']


while count<=no_of_generations:
    next_gen = []
    #----SELECTION-----#
    next_gen.append(pop_fit[0]['chromosome'])#elitism, to pick the best fitness
    pop_fit[0]['flag'] = True
    selection()
    
    #--CROSSOVER THE MATING POOL AND WE GET OUR NEXT GENERATION
    crossover()
    
    # -----------------------------MUTATION---------------------------
    mutation()

    #remapping into range to correct overflow produced during mutation and crossover
    scale(1,UPPER_LIMIT,LOWER_LIMIT,POPULATION_SIZE,7,next_gen)

    population=next_gen
    get_fitness()
    pop_fit = np.sort(pop_fit,order='fitness')[::-1]
    count+=1

print '------------------------------final population------------------'
print pop_fit['chromosome']
print '------------------------------optimal solution is --------------'
print pop_fit['chromosome'][0]

#plt.scatter(range(POPULATION_SIZE),scaled_population)
#plt.scatter(range(POPULATION_SIZE),fitness_list)
#plt.show()