def slope(value_x,value_y):
    n=len(value_x)
    k=0
    avg_slope=0
    while k<n:
        avg_slope+=value_y[k]/value_x[k]
        k+=1
    return avg_slope/n

def slope_2(value_x,value_y):
    n=len(value_x)
    k=1
    x1=value_x[0]
    y1=value_y[0]
    avg_slope=0
    while k<n:
        x2=value_x[k]
        y2=value_y[k]
        avg_slope+=(y2-y1)/(x2-x1)
        y1=y2
        x1=x2
        k+=1
    return avg_slope/(n-1)

def intercept(avg_slope,value_x,value_y):
    b=0
    n=len(value_x)
    k=0
    while k<n:
        b+= value_y[k]-value_x[k]*avg_slope
        k+=1
    return b/n

def height(m,x,b):
    return m*x+b

x=[1700,2100,1900,1300,1600,2200]
y=[53000,44000,59000,82000,50000,68000]

slp=slope_2(x,y)
intr=intercept(slp,x,y)
print("y=",slp,"x+",intr)
x_val=input("what is the square footage? ")
y_val=height(slp,float(x_val),intr)
print ("The house should cost $",round(y_val,2))

import pylab
import numpy

fx = numpy.linspace(min(x),max(x),100) # 100 linearly spaced numbers
fy = slp*fx+intr # computing the values of sin(x)/x

import matplotlib.pyplot as plt
plt.plot(fx, fy)
plt.scatter(x,y)
plt.show()