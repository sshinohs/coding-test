import sys

input = sys.stdin.readline

def fibo(n):
    arr = [0, 1]
    if n < 2:
        return arr[n]
    for _ in range(2, n+1):
        arr.append(arr[-2]+arr[-1])
    return arr[-1]


print(fibo(int(input())))