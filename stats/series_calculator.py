import math
def series_sum(frac):
    k,n=1,1000
    sum_i=0
    while k<n:
        sum_i+=math.pow(frac,k)
        #print(sum_i)
        k+=1
    return sum_i
p_tot=(1/6)*series_sum(5./6.)
print(p_tot)