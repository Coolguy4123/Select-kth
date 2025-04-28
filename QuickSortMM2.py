import random
import time
import math

def gen_lst(A,n):
    for i in range(n):
        A.append(random.randint(0,100))

# def return_kth(A,k):
#     return A[k-1]

# def find_median(A, p, r):
#     tmp = []
#     for i in range(p, r+1):
#         tmp.append(A[i])
#     tmp.sort()
#     return tmp[(r-p+1)//2]

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
    
    v = select2(M,n//r,(n//r)//2)
    # Parition
    ppos = partition
    
    #Cases
    if k = ppos:


    


def partition(A, p, q, mm):
    for i in range(p,q+1):
        if A[i] == mm:
            A[i], A[q] = A[q], A[i]
            break

    i = p - 1
    for j in range(p, q):
        if A[j] <= A[q]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[q] = A[q], A[i+1]

def quickSort(A,p,q):
    if p < q:
        pivotPos = partition(A,p,q)
        quickSort(A,p,pivotPos-1)
        quickSort(A,pivotPos+1,q)

def select(A,n,k):
    r = 5
    if n <= r:
        # quickSort(A,0,n-1)
        # return_kth(A,k)
        return_kth(sorted(A),k)
    

# def partition(A, low, high):
    # v, j = A[low], low
    # for i in range(low + 1, high+1):
    #     if A[i] < v:
    #         j+=1
    #         A[i],A[j] = A[j], A[i]
    # pivotPos = j
    # A[low],A[pivotPos] = A[pivotPos], A[low]
    # return j+1


# Divide into sublists, usually with the length of 5 for each
if __name__ == '__main__':
    N = 5
    k = 2
    arr = []

    gen_lst(arr,N)
    print(arr)

    quickSort(arr,0,N-1)
    print(arr)

    print(f"{k}th smallest element: {return_kth(arr,k)}")