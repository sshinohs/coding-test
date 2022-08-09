from collections import deque
import copy
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))



def bfs(board, N, M, st):
    arr = copy.deepcopy(board)
    q = deque()
    q.append(st)
    arr[st[0]][st[1]] = -1
    
    diff = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        now = q.popleft()
        
        for dif in diff:
            nxt = (now[0] + dif[0], now[1] + dif[1])
            if nxt[0] >= 0 and nxt[0] < N and nxt[1] >= 0 and nxt[1] < M:
                if arr[nxt[0]][nxt[1]] == 0:
                    arr[nxt[0]][nxt[1]] = -1
                    q.append(nxt)
                elif arr[nxt[0]][nxt[1]] >= 1:
                    arr[nxt[0]][nxt[1]] += 1
                    if arr[nxt[0]][nxt[1]] == 3:
                        board[nxt[0]][nxt[1]] = 0

count = 0

while True:
    count += 1
    bfs(board, N, M, (0, 0))
    check = 0
    if sum(map(sum, board)) == 0:
        break

print(count)
