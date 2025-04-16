import random
import time

def gen_lst(arr,n):
    for i in range(n):
        arr.append(random.randint(0,100))

def return_kth(arr,k):
    return arr[k-1]

if __name__ == '__main__':
    N = 20
    arr = []

    gen_lst(arr,N)
    print(arr)