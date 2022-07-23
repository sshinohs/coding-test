import sys

input = sys.stdin.readline

def prime_arr(n):
    primes = [1] * (n+1)
    primes[0] = 0
    primes[1] = 0

    if n < 2:
        return primes
    
    for i in range(2, n+1):
        if primes[i] == 1:
            count = 2
            while count * i <= n:
                primes[count * i] = 0
                count += 1
    return primes

def goldbach(primes, n):

    for i in range(n//2, n):
        if primes[i] == 1 and primes[n-i] == 1:
            return i, n-i

n_max = 10000

primes = prime_arr(n_max)

T = int(input())

for _ in range(T):
    num = int(input())
    a, b = goldbach(primes, num)
    print(b, a)