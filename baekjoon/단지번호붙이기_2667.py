import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

board = []

for _ in range(N):
    board.append(input().strip())

visited = [[0] * N for _ in range(N)]

count_complex = 0
complex_size = []

def dfs(i, j):

    diff = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    st = (i, j)
    stack = deque()

    size = 0
    stack.append(st)

    while stack:
        now = stack.pop()
        if visited[now[0]][now[1]] == 0:
            visited[now[0]][now[1]] = 1
            size += 1
            for dif in diff:
                nxt = (now[0] + dif[0], now[1] + dif[1])
                if nxt[0] >= 0 and nxt[0] < N and nxt[1] >= 0 and nxt[1] < N:
                    if visited[nxt[0]][nxt[1]] == 0 and board[nxt[0]][nxt[1]] == '1':
                        stack.append((nxt[0], nxt[1]))
    
    return size


for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and board[i][j] == '1':
            count_complex += 1
            complex_size.append(dfs(i, j))

complex_size.sort()

print(count_complex)
for i in complex_size:
    print(i)