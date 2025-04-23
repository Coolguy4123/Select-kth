import random
import time

def gen_lst(A,n):
    for i in range(n):
        A.append(random.randint(0,100))

def return_kth(A,k):
    return A[k-1]

def quickSort(A,p,q):
    if p < q:
        pivotPos = partition(A,p,q)
        quickSort(A,p,pivotPos-1)
        quickSort(A,pivotPos+1,q)

def partition(A, low, high):
    v, j = A[low], low
    for i in range(low + 1, high+1):
        if A[i] < v:
            j+=1
            A[i],A[j] = A[j], A[i]
    pivotPos = j
    A[low],A[pivotPos] = A[pivotPos], A[low]
    return j+1


if __name__ == '__main__':
    N = 5
    k = 2
    arr = []

    gen_lst(arr,N)
    print(arr)

    quickSort(arr,0,N-1)
    print(arr)

    print(f"{k}th smallest element: {return_kth(arr,k)}")