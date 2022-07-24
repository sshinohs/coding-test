import sys

input = sys.stdin.readline

N = int(input())

def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    arr = [1, 2]
    for _ in range(2, n):
        arr.append((arr[-2]+arr[-1])%15746)
    return arr[-1]

print(fibo(N))