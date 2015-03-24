import random
k,n=0,100000
sum_x=0
sum_y=0
sum_diff=0
while k<n:
    x=random.random()
    y=random.random()
    sum_x+=x
    sum_y+=y
    sum_diff+=abs(x-y)
    k+=1
print(sum_x/n,sum_y/n,sum_diff/n)
