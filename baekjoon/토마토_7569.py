import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

cube = []
for _ in range(H):
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    cube.append(board)


def bfs(arr):
    len_arr = (len(arr), len(arr[0]), len(arr[0][0]))
    q = deque()
    for k in range(len_arr[0]):
        for i in range(len_arr[1]):
            for j in range(len_arr[2]):
                if arr[k][i][j] == 1:
                    q.append((k, i, j))

    diff = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    while q:
        now = q.popleft()
        for dif in diff:
            nxt = (now[0] + dif[0], now[1] + dif[1], now[2] + dif[2])
            if nxt[0] >= 0 and nxt[0] < len_arr[0] and nxt[1] >= 0 and nxt[1] < len_arr[1] and nxt[2] >= 0 and nxt[2] < len_arr[2]:
                if arr[nxt[0]][nxt[1]][nxt[2]] == 0:
                    arr[nxt[0]][nxt[1]][nxt[2]] = arr[now[0]][now[1]][now[2]] + 1
                    q.append(nxt)

    check_max = 0
    for k in range(len_arr[0]):
        for i in range(len_arr[1]):
            for j in range(len_arr[2]):
                if arr[k][i][j] == 0:
                    return -1
                if  check_max < arr[k][i][j]:
                    check_max = arr[k][i][j]
    
    return check_max-1

print(bfs(cube))