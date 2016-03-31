from random import randrange,uniform
#import matplotlib.pyplot as plt
import numpy as np
import math as m


#~~~~~~~~~~~~~~~~~~~~~VARIABLES~~~~~~~~~~~~~~~~~
POPULATION_SIZE = 51
LENGTH_OF_BIT_STRING = 32
crossover_probability = 0.5
Mutation_probability = 0.01
LOWER_LIMIT = [0,0]
UPPER_LIMIT = [2,2]
no_of_generations =100
count =0
fitness_track = []
fitness_average = []
bit_length = []
type_fitness = [('chromosome_x',int),('chromosome_y',int), ('fitness',float),('flag',bool)]
type_solution = [('x',float),('y',float)]

precsion_level= 100
no_of_variables = 2
next_gen_x = []
next_gen_y = []
next_gen = [next_gen_x,next_gen_y]
matingpool_x=[]
matingpool_y=[]
matingpool = [matingpool_x,matingpool_y]
population_x = []
population_y = []
population = [population_x,population_y]



 # TODO auto generate of list of lists and data type for np arrays
 # TODO fix scaling of negative limits
#~~~~~~~~~~~~~~~~~~~~~~FUNCTIONS~~~~~~~~~~~~~~~~~~~~
def fitness(x,y):
    x=x/float(precsion_level)
    y=y/float(precsion_level)
    #return 1601-((1-x)*(1-x)+100*(y-x*x)*(y-x*x))
    #return 46-(20+x*x+y*y-10*(m.cos(2*m.pi*x)+m.cos(2*m.pi*x)))
    return x*x + y*y

def population_generation(population):
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
        population[i] = LOWER_LIMIT*precsion_level+population[i]*((UPPER_LIMIT*precsion_level-LOWER_LIMIT*precsion_level)/float(2**LENGTH_OF_BIT_STRING-1))
        population[i] = int(population[i])

def get_fitness():
    for i in range(0,POPULATION_SIZE):
        pop_fit[i] = (population[0][i],population[1][i],fitness(population[0][i],population[1][i]),False)

def selection():
    while len(matingpool[0])<POPULATION_SIZE-1:
        temp = randrange(1,POPULATION_SIZE)
        if(pop_fit[temp]['flag']==False):
            for i in range(no_of_variables):
                matingpool[i].append(pop_fit[temp][i])
                pop_fit[temp]['flag'] = True

def crossover(matingpool,bit_length,next_gen):
    for i in range(0,POPULATION_SIZE-1,2):
        for j in range(bit_length):
            if(uniform(0,1)>crossover_probability):
                if((matingpool[i] & 2**((bit_length-1)-j))!=(matingpool[i+1] & 2**((bit_length-1)-j))): #checking for inequality of bits
                    matingpool[i] = matingpool[i]^2**((bit_length-1)-j) #swapping bits
                    matingpool[i+1] = matingpool[i+1]^2**((bit_length-1)-j) #swapping bits
        next_gen.append(matingpool[i])
        next_gen.append(matingpool[i+1])

def mutation(next_gen,bit_length):
    for i in range(1,POPULATION_SIZE):
        for j in range(bit_length):
            if(uniform(0,1)<Mutation_probability):
                next_gen[i]=next_gen[i]^2**((bit_length-1)-j)

def get_solution():
    for i in range(POPULATION_SIZE):
        solution[i][0] = pop_fit[i][0]/float(precsion_level)
        solution[i][1] = pop_fit[i][1]/float(precsion_level)

def get_bit_length():
    for i in range(no_of_variables):
        bit_length.append(len(bin(UPPER_LIMIT[i]*precsion_level))-2)


#~~~~~~~~~~~~~~~~~~~~MAIN~~~~~~~~~~~~~~~~~~~~~~~~~

get_bit_length()
for i in range(no_of_variables):
    population_generation(population[i])

#We now have a initial population of POPULATION_SIZE
#Scale population into Limits
for i in range(no_of_variables):
    scale(0,UPPER_LIMIT[i],LOWER_LIMIT[i],POPULATION_SIZE,LENGTH_OF_BIT_STRING,population[i])

pop_fit = np.zeros((POPULATION_SIZE,),dtype = type_fitness)#Create a structured 1D array to store population and fitness
get_fitness()   #get fitness of chromosomes
pop_fit = np.sort(pop_fit,order='fitness')[::-1]
solution = np.zeros((POPULATION_SIZE,),dtype = type_solution)
print '------------------------------initial population----------------'
get_solution()
print solution

fitness_track.append(float(pop_fit['fitness'][0]))
########################################################
fitness_average.append(float(np.average(pop_fit['fitness'])))
########################################################
while count<=no_of_generations:
    for i in range(no_of_variables):
        next_gen[i] = []

    #----SELECTION-----#
    for i in range(no_of_variables):
        next_gen[i].append(pop_fit[0][i])#elitism, to pick the best fitness
    pop_fit[0]['flag'] = True

    selection()

    #----CROSSOVER-----#
    for i in range(no_of_variables):
        crossover(matingpool[i],bit_length[i],next_gen[i])

    #----MUTATION-----#
    for i in range(no_of_variables):
        mutation(next_gen[i],bit_length[i])

    #remapping into range to correct overflow produced during mutation and crossover
    for i in range(no_of_variables):
        scale(1,UPPER_LIMIT[i],LOWER_LIMIT[i],POPULATION_SIZE,bit_length[i],next_gen[i])

    for i in range(no_of_variables):
        population[i]=next_gen[i]

    get_fitness()
    pop_fit = np.sort(pop_fit,order='fitness')[::-1]
    fitness_track.append(float(pop_fit['fitness'][0]))
    fitness_average.append(float(np.average(pop_fit['fitness'])))
    count+=1

print '------------------------------final population------------------'
get_solution()
print solution
print '------------------------------optimal solution is--------------'
print solution[0]
print '--------------------------------improvement---------------------'
print 'initial fitness=%f' %fitness_track[0]
print 'final fitness=%f' %pop_fit[0]['fitness']
print 'improvement in fitness = %f' %(pop_fit[0]['fitness']-fitness_track[0])
print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
avg_fitness_inc_count=0
for i in range(len(fitness_average)-1):
    if fitness_average[i+1]>fitness_average[i]:
        avg_fitness_inc_count+=1

print 'avg fitness incresed %d times' %avg_fitness_inc_count
#plt.scatter(range(no_of_generations+2),fitness_track)
#plt.scatter(range(no_of_generations+2),fitness_average)
#plt.show()
