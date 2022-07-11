import sys
import math

input = sys.stdin.readline

M, N = map(int, input().split())

# M = 3
# N = 16

# n = int(input())

def prime_check(n):
    if n == 1:
        return False
    
    if n == 2:
        return True

    limit = math.ceil(math.sqrt(n))

    for i in range(2, limit+1):
        if n % i == 0:
            return False
    return True

for i in range(M, N+1):
    if prime_check(i):
        print(i)

# print(prime_check(n))

# def prime_arr(n):
#     1


# def prime_check(n):
    