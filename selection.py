from random import uniform
import matplotlib.pyplot as plt
#import numpy.array as np

POPULATION_SIZE = 100
LENGTH_OF_BIT_STRING = 32
LOWER_LIMIT = 0
UPPER_LIMIT = 100


population = []
scaled_population =[]
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
for val in population:
    val *= LOWER_LIMIT+((UPPER_LIMIT-LOWER_LIMIT)/float(2**LENGTH_OF_BIT_STRING-1))
    scaled_population.append(int(val))
print(scaled_population)
#Now our Population should be scaled according to our limits
#print(population)
#plt.scatter(range(POPULATION_SIZE),scaled_population)
#plt.show()
