import sys
import math

input = sys.stdin.readline

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    
    check_limit = math.ceil(math.sqrt(n))+1

    for i in range(2, check_limit):
        if n % i == 0:
            return False
    return True

M = int(input())
N = int(input())

primes_sum = 0
primes_min = 0
for i in range(M, N+1):
    if is_prime(i):
        primes_sum += i
        if primes_min == 0:
            primes_min = i

if primes_min:
    print(primes_sum)
    print(primes_min)
else:
    print(-1)