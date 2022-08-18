import sys
from itertools import product

input = sys.stdin.readline

N, M = map(int, input().split())

candidates = list(range(1, N+1))

for nums in product(candidates, repeat = M):
    for num in nums:
        print(num, end=' ')
    print()