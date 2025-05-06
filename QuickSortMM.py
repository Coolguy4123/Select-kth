import random
import time

#------------------------------------------------------------------------------------
#---Generates a an array with size N filled with values between 0 to 100 inclusive---
#------------------------------------------------------------------------------------
def gen_lst(A,n):
    for i in range(n):
        A.append(random.randint(0,100))

#-------------------------------------
#---Return the kth smallest element---
#-------------------------------------
def return_kth(A,k):
    return A[k-1]

#--------------------------------------------------------
# Step of finding median of medians
# 1) Split the array into subsets of 5
# 2) Sort each of the subsets in ascending order
# 3) Finds the median of medians using Divide and Conquer 
#--------------------------------------------------------
def mm(A, p, q, r = 5):
    n = q - p + 1
    if n <= r:
        A.sort()
        return A[n//2]
    
    subsets = [A[i:i+r] for i in range(0,n,r)]

    medians = []
    for i in subsets:
        i.sort()
        medians.append(i[len(i)//2])

    return mm(medians, 0, len(medians)-1, r)

#----------------------------------------------------------------
#---Partioning step for QuickSortMM, but based on what pval is---
#----------------------------------------------------------------
def partition(A, p, q, pval):
    for i in range(p,q+1):
        if A[i] == pval:
            A[p], A[i] = A[i], A[p]
            break
    
    pivot, i = A[p], p
    for j in range(p+1, q+1):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[p], A[i] = A[i], A[p]
    return i

#------------------------------------------------------------------------------
#---Divide and Conquer for QuickSort MM, with position based on what pVal is---
#------------------------------------------------------------------------------
def quickSortMM(A,p,q):
    if p < q:
        pVal = mm(A, p, q)
        ppos = partition(A, p, q, pVal)
        quickSortMM(A, p, ppos-1)
        quickSortMM(A, ppos+1, q)


if __name__ == '__main__':
    # Initialization
    N = 2
    k = 1
    arr = []

    # Randomize array
    gen_lst(arr,N)

    # Timing of the algorithm
    start = time.time()
    quickSortMM(arr,0,N-1)
    return_kth(arr,k)
    timeElapsed = time.time() - start

    # Outputs
    print(f"---Time elapsed = {timeElapsed} seconds")
    print(f"\n{k}th smallest element: {return_kth(arr,k)}\n")