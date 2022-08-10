import sys
import heapq

input = sys.stdin.readline

N = int(input())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

for i, row in enumerate(board):
    if 9 in row:
        st = (i, row.index(9))

board[st[0]][st[1]] = 0

diff = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def bfs(board, diff, N, st, size):
    ii, jj = st
    visited = [[0] * N for _ in range(N)]
    h = []
    heapq.heappush(h, (0, ii, jj))
    visited[ii][jj] = 0

    while h:
        dist, now_ii, now_jj = heapq.heappop(h)
        if board[now_ii][now_jj] > 0 and board[now_ii][now_jj] < size:
            board[now_ii][now_jj] = 0
            return (dist, now_ii, now_jj)
        
        for dif in diff:
            nxt_ii = now_ii + dif[0]
            nxt_jj = now_jj + dif[1]
            if nxt_ii >= 0 and nxt_ii < N and nxt_jj >= 0 and nxt_jj < N:
                if visited[nxt_ii][nxt_jj] == 0 and board[nxt_ii][nxt_jj] <= size:
                    visited[nxt_ii][nxt_jj] = 1
                    heapq.heappush(h, (dist + 1, nxt_ii, nxt_jj))
    
    return (-1, now_ii, now_jj)

pos = st
size = 2
belly = 0
total_dist = 0

while True:
    dist, pos_ii, pos_jj = bfs(board, diff, N, pos, size)
    pos = (pos_ii, pos_jj)
    if dist == -1:
        print(total_dist)
        break
    total_dist += dist
    belly += 1

    if belly == size:
        size += 1
        belly = 0
