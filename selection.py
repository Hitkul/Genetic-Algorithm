#Generate Random Numbers
from random import uniform
import matplotlib.pyplot as plt
from math import pow
#Assuming we're generating 8 bit integers only
population = []

limit_lower=0;
limit_upper=100;

for j in range(100):
    sample = []
    for i in range(32):
        if(uniform(0,1)<0.5):
           sample.append('0')#builds a list of strings
        else:
           sample.append('1')
    stringified_sample = ''.join(sample)#converts list of strings into string
    foo1=int(stringified_sample,2);#converts string into binary
    foo2=(limit_lower+((limit_upper-limit_lower)/float(2**32-1)))#finding the equivalent value in range  
    population.append(foo2*foo1)#generating initial population 

print(min(population))
print(max(population))

#At this point we have generated a population of 100 random integers
print(population)

plt.scatter(range(100),population)
plt.show()
