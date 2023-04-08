import sys

input = sys.stdin.readline

N, M = map(int, input().split())

buckets = list(range(1, N+1))

for _ in range(M):
    a, b = map(int, input().split())
    if a-2 != -1:
        buckets[a-1:b] = buckets[b-1:a-2:-1]
    else:
        buckets[a-1:b] = buckets[b-1::-1]

for num in buckets:
    print(num, end=' ')

