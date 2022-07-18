import sys

input = sys.stdin.readline

N, K = map(int, input().split())

stuff = [(0, 0)]
sheet = [[0] * (K+1) for _ in range(N+1)]

for _ in range(N):
    stuff.append(tuple(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        w = stuff[i][0]
        v = stuff[i][1]

        if j < w:
            sheet[i][j] = sheet[i-1][j]
        else:
            sheet[i][j] = max(sheet[i-1][j], sheet[i-1][j-w]+v)

print(sheet[N][K])