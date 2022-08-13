from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

Ns = [i for i in range(1, N+1)]

for i in combinations(Ns, M):
    for j in i:
        print(j, end=' ')
    print()