import sys
input = sys.stdin.readline

N, M = map(int, input().split())

a = set()
for _ in range(N):
    a.add(input().strip())

count = 0
for _ in range(M):
    if input().strip() in a:
        count += 1

print(count)