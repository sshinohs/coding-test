import sys

input = sys.stdin.readline

N, M = map(int, input().split())

buckets = [0]*N

for _ in range(M):
    i, j, k = map(int, input().split())
    buckets[i-1:j] = [k]*(j-i+1)

for num in buckets:
    print(num, end=' ')