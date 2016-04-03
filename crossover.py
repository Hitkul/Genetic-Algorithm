from random import randrange,uniform
import matplotlib.pyplot as plt
import numpy as np
import math as m


 # TODO MOGA
#~~~~~~~~~~~~~~~~~~~~~VARIABLES~~~~~~~~~~~~~~~~~
POPULATION_SIZE = 51
LENGTH_OF_BIT_STRING = 32
crossover_probability = 0.5
Mutation_probability = 0.01
no_of_try_in_hillclimbing = 20
reproduction_ratio=(int)(10*POPULATION_SIZE/100)
if reproduction_ratio == 0:
    reproduction_ratio = 1
crossover_ratio= (int)(85*POPULATION_SIZE/100)
if crossover_ratio % 2 != 0:
    crossover_ratio -=1;
mutation_ratio= POPULATION_SIZE - (reproduction_ratio+crossover_ratio)
########################################################
print reproduction_ratio
print crossover_ratio
print mutation_ratio
########################################################
LOWER_LIMIT = [0,0]
UPPER_LIMIT = [3,3]
no_of_generations =175
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
left_for_mutation_x = []
left_for_mutation_y = []
left_for_mutation = [left_for_mutation_x,left_for_mutation_y]



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

def scale(start_point,UPPER_LIMIT,LOWER_LIMIT,POPULATION_SIZE,UPPER_LIMIT_current,LOWER_LIMIT_current,population):
    for i in range(start_point,POPULATION_SIZE):
        #population[i] = LOWER_LIMIT*precsion_level+population[i]*((UPPER_LIMIT*precsion_level-LOWER_LIMIT*precsion_level)/float(2**LENGTH_OF_BIT_STRING-1))
        population[i] = (((population[i] - LOWER_LIMIT_current) * (UPPER_LIMIT*precsion_level - LOWER_LIMIT*precsion_level)) / (UPPER_LIMIT_current - LOWER_LIMIT_current)) + LOWER_LIMIT*precsion_level
        population[i] = int(population[i])

def get_fitness():
    for i in range(0,POPULATION_SIZE):
        pop_fit[i] = (population[0][i],population[1][i],fitness(population[0][i],population[1][i]),False)

def selection():
    while len(matingpool[0])<crossover_ratio:
        temp = randrange(3,POPULATION_SIZE)
        if(pop_fit[temp]['flag']==False):
            for i in range(no_of_variables):
                matingpool[i].append(pop_fit[temp][i])
                pop_fit[temp]['flag'] = True

def crossover(matingpool,bit_length,next_gen,check):

    for i in range(0,crossover_ratio,2):
        counter = 0
        breaker = True
        temp1=matingpool[i]
        temp2=matingpool[i+1]

        before_diffrence1 = find_diffrence(next_gen[0],temp1)
        before_diffrence2 = find_diffrence(next_gen[0],temp2)

        while (counter<no_of_try_in_hillclimbing) and (breaker==True):


            for j in range(bit_length):
                if(uniform(0,1)>crossover_probability):
                    if((temp1 & 2**((bit_length-1)-j))!=(temp2 & 2**((bit_length-1)-j))): #checking for inequality of bits
                        temp1 = temp1^2**((bit_length-1)-j) #swapping bits
                        temp2 = temp2^2**((bit_length-1)-j) #swapping bits

            after_diffrence1 = find_diffrence(next_gen[0],temp1)
            after_diffrence2 = find_diffrence(next_gen[0],temp2)

            if (after_diffrence1 < before_diffrence1) and (after_diffrence2 < before_diffrence2):
                next_gen.append(temp1)
                next_gen.append(temp2)
                breaker = False
            counter+=1

        if counter == no_of_try_in_hillclimbing:
            next_gen.append(matingpool[i])
            next_gen.append(matingpool[i+1])

def find_diffrence(no1, no2):
    if no1 < no2 :
        return abs(no2 - no1)
    else:
        return abs(no1-no2)

def mutation(left_for_mutation,bit_length):
    for i in range(mutation_ratio):
        for j in range(bit_length):
            if(uniform(0,1)<Mutation_probability):
                left_for_mutation[i]=left_for_mutation[i]^2**((bit_length-1)-j)

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
    scale(0,UPPER_LIMIT[i],LOWER_LIMIT[i],POPULATION_SIZE,max(population[i]),min(population[i]),population[i])

pop_fit = np.zeros((POPULATION_SIZE,),dtype = type_fitness)#Create a structured 1D array to store population and fitness
get_fitness()   #get fitness of chromosomes
pop_fit = np.sort(pop_fit,order='fitness')[::-1]
solution = np.zeros((POPULATION_SIZE,),dtype = type_solution)
print '------------------------------initial population----------------'
get_solution()
print solution

fitness_track.append(float(pop_fit['fitness'][0]))

fitness_average.append(float(np.average(pop_fit['fitness'])))

while count<=no_of_generations:
    print 'generation   ' + str(count)
    for i in range(no_of_variables):
        next_gen[i] = []

    #----REPRODUCTION-----#
    for j in range(reproduction_ratio):
        for i in range(no_of_variables):
            next_gen[i].append(pop_fit[j][i])#elitism, to pick the best fitness
        pop_fit[j]['flag'] = True


    #----SELECTION-----#
    selection()


    #----CROSSOVER-----#
    for i in range(no_of_variables):
        crossover(matingpool[i],bit_length[i],next_gen[i],i)


    #----MUTATION-----#
    for i in range(POPULATION_SIZE):
        if pop_fit[i]['flag']== False:
            for j in range(no_of_variables):
                left_for_mutation[j].append(pop_fit[i][j])

    for i in range(no_of_variables):
        mutation(left_for_mutation[i],bit_length[i])

    for i in range(no_of_variables):
        for j in range(mutation_ratio):
            next_gen[i].append(left_for_mutation[i][j])



    #remapping into range to correct overflow produced during mutation and crossover
    for i in range(no_of_variables):
        scale(1,UPPER_LIMIT[i],LOWER_LIMIT[i],POPULATION_SIZE,max(next_gen[i]),min(next_gen[i]),next_gen[i])

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

plt.scatter(range(no_of_generations+2),fitness_track)
plt.show()
plt.scatter(range(no_of_generations+2),fitness_average)
plt.show()
