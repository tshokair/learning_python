import math
def mean(data):
    return sum(data)/len(data)
def median(data):
    a=sorted(data)
    b=int(len(data)/2)
    return a[b]
def mode(data):
    k=0
    max_num_occurances=0
    mode=data[0]
    while k<len(data):
        num_occurances=data.count(data[k])
        if num_occurances>max_num_occurances:
            max_num_occurances=num_occurances
            mode=data[k]
        k+=1
    return mode
def variance(data):
    #avg=mean(data)
    #return sum([(a-avg)*(a-avg) for a in data])/len(data)
    return sum([a*a for a in data])/len(data)-sum(data)*sum(data)/(len(data)*len(data))
def standard_deviation(data):
    return math.sqrt(variance(data))
def new_mean(oldmean,n,x):
    return (n*oldmean+x)/(n+1)

house_prices_1=[170000,190000,165000,180000,165000]
house_prices_2=[2400000,125000,148000,160000,110000,325000,180000]
age=[4,3,32,33,4,32,3,38,4,35,36]
nums=[ 5, 9, 100, 9, 97, 6, 9, 98, 9]
nums_2=[3, 9, 3, 8, 2, 9, 1, 9, 2, 4]
nums_3=[3,4,5,6,7]
nums_4=[8,9,10,11,12]
nums_4_1=[8,9,10,11,12,8]
nums_5=[15,20,25,30,35]
nums_6=[3,3,3,3,3]
friends=[17,19,18,17,19]
family=[7,38,4,23,18]
data1=[1,2,5,10,-20,5,5]
data2=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]
list_of_interest=nums_4_1
print("mean:",mean(list_of_interest))
print("new mean",new_mean(mean(list_of_interest),len(list_of_interest),8))
print("median:",median(list_of_interest))
print("mode",mode(list_of_interest))
print("variance",variance(list_of_interest))
print("standard deviation",standard_deviation(list_of_interest))