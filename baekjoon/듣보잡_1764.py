import sys
input = sys.stdin.readline

N, M = map(int, input().split())

d = {}
d_b = []
for _ in range(N):
    d[input()[:-1]] = 1

for _ in range(M):
    name = input()[:-1]
    if name in d:
        d_b.append(name)

print(len(d_b))
d_b.sort()
for name in d_b:
    print(name)