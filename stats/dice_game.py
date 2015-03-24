import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
def roll():
    x=random.random()*6.0
    if x<1:
        return 1
    elif x>=1 and x<2:
        return 2
    elif x>=2 and x<3:
        return 3
    elif x>=3 and x<4:
        return 4
    elif x>=4 and x<5:
        return 5
    elif x>=5:
        return 6


win1=0
win2=0
k=0
n=500000
d_rolls=[]
while k<n:
    win=False
    while win!=True:
        x=roll()
        d_rolls.append(x)
        if x==6:
            win=True
            win1+=1
        else:
            x=roll()
            d_rolls.append(x)
            if x==6:
                win=True
                win2+=1
    k+=1
plt.hist(d_rolls)
print("In",n,"games player 1 won",win1," times and player 2 won",win2,"times")
print("propability player 1 wins is",win1/n)
plt.show()
