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

#--------------------------------------------
#---Divide and Conquer Step for Quick Sort---
#--------------------------------------------
def quickSort(A,p,q):
    if p < q:
        pivotPos = partition(A,p,q)
        quickSort(A,p,pivotPos-1)
        quickSort(A,pivotPos+1,q)

#--------------------------------------------------------------
#---Partioning step of QuickSort, based on the first element---
#--------------------------------------------------------------
def partition(A, low, high):
    v, j = A[low], low
    for i in range(low + 1, high+1):
        if A[i] < v:
            j+=1
            A[i],A[j] = A[j], A[i]
    pivotPos = j
    A[low],A[pivotPos] = A[pivotPos], A[low]
    return j


if __name__ == '__main__':
    # Initialization
    N = 2
    k = 1
    arr = []

    # Randomize the list
    gen_lst(arr,N)

    # Timing of the algrithm
    start = time.time()
    quickSort(arr,0,N-1)
    return_kth(arr,k)
    timeElapsed = time.time() - start

    # Outputs
    print(f"---Time elapsed = {timeElapsed} seconds")
    print(f"\n{k}th smallest element: {return_kth(arr,k)}\n")