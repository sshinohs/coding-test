import sys

input = sys.stdin.readline

def factorial(n):
    arr = []
    arr.append(1)
    arr.append(1)
    for i in range(2,n+1):
        arr.append(arr[-1]*i)
    return arr

N, K = map(int, input().split())

arr = factorial(N)

print(arr[N]//arr[K]//arr[N-K])


