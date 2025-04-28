import random
import time
import math

def gen_lst(A,n):
    for i in range(n):
        A.append(random.randint(0,100))


def partition(A, low, high, piv):
    j = low
    for i in range(low + 1, high+1):
        if A[i] < piv:
            j+=1
            A[i],A[j] = A[j], A[i]
    pivotPos = j
    A[low],A[pivotPos] = A[pivotPos], A[low]
    return j+1


def select2(A,n,k,r=5):
    if n <= r:
        A.sort()
        return A[k-1]
    
    subsets = [A[i:i+r] for i in range(0,n,r)] #Divide into subsets

    #Find medians of each subset
    medians = []

    for i in subsets:
        i.sort()
        medians.append(i[len(i)//2])
    
    v = select2(medians,n//r,(n//r)//2)
    
    # Parition
    ppos = partition(A,0,n,v)

    #Cases
    if k == ppos:
        return v
    elif k < ppos:
        S = A[1:ppos]
        return select2(S,ppos-1,k)
    else:
        R = A[ppos+1,n]
        return select2(R,n-ppos,k-ppos)


# Divide into sublists, usually with the length of 5 for each
if __name__ == '__main__':
    N = 5
    k = 2
    arr = []

    gen_lst(arr,N)
    print(arr)

    kS = select2(arr,N,k)
    print(arr)
    print(kS)
    # print(f"{k}th smallest element: {return_kth(arr,k)}")