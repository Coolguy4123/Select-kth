import random
import time

def gen_lst(A,n):
    for i in range(n):
        A.append(random.randint(0,100))

def return_kth(A,k):
    return A[k-1]

def merge(A, low, mid, high):
    U = [0] * len(A)
    i,j,k = low, mid+1, low
    while i <= mid and j <= high:
        if A[i] < A[j]:
            U[k] = A[i]
            i += 1
        else:
            U[k] = A[j]
            j += 1
        k += 1
    
    if i > mid: #If there are remaining elements in upper half
        for x in range(j,high+1):
            U[k] = A[x]
            k += 1
    else:
        for x in range(i,mid+1):
            U[k] = A[x]
            k += 1
    for p in range(low, high+1):
        A[p] = U[p]

def mergeSort(A,low,high):
    if low < high:
        mid = (low + high) // 2
        mergeSort(A, low, mid)
        mergeSort(A, mid+1, high)
        merge(A, low, mid, high)

if __name__ == '__main__':
    N = 5
    k = 2
    arr = []

    print("\nMerge Sort")
    print("------------------------")
    # gen_lst(arr,N)
    arr = [27,71,45,76,1]
    print(f"Original Array: {arr}")

    mergeSort(arr,0,N-1)
    print(f"Sorted Array: {arr}")
    print(f"\n{k}th smallest element: {return_kth(arr,k)}\n")