import math
import random
def binarySearch(alist, item):
    n=len(alist)
    n_sub=n
    first = 0
    last=n-1
    found=False
    index=0
    k=0
    while n_sub>1:
        #print("loop #",k,"looking from index",first,"to",last,"n_sub=",n_sub)
        k+=1
        if first==last:
            return first
        elif item<alist[first]:
            #print ("at index",0)
            found=True
            return first
        elif item>alist[last]:
            #print ("at index",len(alist))
            found=True
            return last+1
        else:
            if n_sub%2==0:
                right=math.ceil((last+first)/2)
                left=(last+first)//2
                #print(left,right)
                if item==alist[right]:
                    found=True
                    return right
                elif item==alist[left]:
                    found=True
                    return left
                elif item<alist[left]:
                    if n_sub>2:
                        n_sub=n_sub//2
                        index=last
                        last=left-1
                    else:
                        return left
                else:
                    if n_sub>2:
                        n_sub=n_sub//2
                        index=first
                        first=right
                    else:
                        return right
            else:
                center=(last+first)//2
                if item==alist[center]:
                    found=True
                    return center
                elif item>alist[center]:
                    first=center+1
                    n_sub=n_sub//2
                    if n_sub==1:
                        return first
                 
                else:
                    n_sub=n_sub//2
                    last=center
                    if n_sub==1:
                        return first

    if n_sub==1:
        return index

def insert_into_list(num_list,num):
    index=binarySearch(num_list,num)
    num_list.insert(index,num)
    return num_list
def order_list(num_list):
    n=len(num_list)
    ordered_list=[]
    ordered_list.insert(0,num_list[0])
    k=1
    while k<n:
        #print("inserting",num_list[k],"in",ordered_list)
        insert_into_list(ordered_list,num_list[k])
        k+=1
    return ordered_list


random_list=[]
k=0
while k<100:
    x=random.random()*100//1
    random_list.append(x)
    k+=1
print(random_list)
new_list=order_list(random_list)
print(new_list)
