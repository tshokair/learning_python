import math
import random
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
def mean(data):
    return sum(data)/len(data)
def variance(data):
    return sum([a*a for a in data])/len(data)-sum(data)*sum(data)/(len(data)*len(data))
def standard_deviation(data):
    return math.sqrt(variance(data))

def flip(N):
   return[random.random()>.5 for x in range (0,N)]
def sample(N):
    return [mean(flip(N)) for x in range (0,N)]

N=1000
outcomes=sample(N)
plt.hist(outcomes,bins=30)
print (mean(outcomes))
print (standard_deviation(outcomes))
plt.show()
