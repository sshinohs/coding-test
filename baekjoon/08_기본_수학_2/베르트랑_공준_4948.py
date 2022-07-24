import sys

input = sys.stdin.readline

def prime_arr(n):
    prime_board = [1] * (n + 1)
    prime_board[0] = 0
    prime_board[1] = 0
    
    if n < 2:
        return prime_board
    
    for i in range(2, n+1):
        if prime_board[i] == 1:
            count = 2
            while i*count <= n:
                prime_board[i*count] = 0
                count += 1
    return prime_board

max_n = 123456

primes = prime_arr(max_n*2)

cumul_primes = [0]
for i in primes:
    cumul_primes.append(cumul_primes[-1]+i)

while True:
    n = int(input())
    if n == 0:
        break
    print(cumul_primes[2*n+1] - cumul_primes[n+1])