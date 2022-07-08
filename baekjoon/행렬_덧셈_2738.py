import sys

input = sys.stdin.readline

N, M = map(int, input().split())

a = []
for _ in range(N):
    a.append(list(map(int, input().split())))

b = []
for _ in range(N):
    b.append(list(map(int, input().split())))


for i in range(N):
    for j in range(M):
        print(a[i][j] + b[i][j], end=' ')
    print()