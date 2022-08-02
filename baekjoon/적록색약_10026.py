import sys
import copy
from collections import deque

input = sys.stdin.readline

N = int(input())

board = []
for _ in range(N):
    board.append(list(input().strip()))

board_b = copy.deepcopy(board)

def dfs(arr, st, color_a, color_b):
    stack = deque()
    stack.append(st)

    diff = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while stack:
        now = stack.pop()
        arr[now[0]][now[1]] = 'N'
        
        for dif in diff:
            nxt = (now[0] + dif[0], now[1] + dif[1])
            if nxt[0] >= 0 and nxt[0] < N and nxt[1] >= 0 and nxt[1] < N:
                if arr[nxt[0]][nxt[1]] == color_a or arr[nxt[0]][nxt[1]] == color_b:
                    stack.append(nxt)

count = 0
for i in range(N):
    for j in range(N):
        if board[i][j] != 'N':
            count += 1
            dfs(board, (i, j), board[i][j], board[i][j])

count_b = 0
for i in range(N):
    for j in range(N):
        if board_b[i][j] == 'R' or board_b[i][j] == 'G':
            count_b += 1
            dfs(board_b, (i, j), 'R', 'G')
        elif board_b[i][j] == 'B':
            count_b += 1
            dfs(board_b, (i, j), 'B', 'B')

print(count, count_b)