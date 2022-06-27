import sys

input = sys.stdin.readline

N, K = map(int, input().split())

if K <= N:
    print(N-K)
else:
    count = 0
    while N*2**count < K:
        count += 1
    
    a = N*2**count - K
    b = K - N*2**(count-1)

    if b <= a:
        count -= 1
        print('b')
        num = b
    else:
        print('a')
        num = a
    
    count_n = 0
    for i in range(count, -1, -1):
        quotient = num // 2 ** i
        remainder = num % 2 ** i
        if remainder > 2 ** (i-1):
            count_n += quotient - 1
            num = abs(remainder - 2 ** (i-1))
        else:
            count_n += quotient
            num = remainder
    print(count + count_n)