import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, list(input().strip()))))

# print(board)

start = (0, 0)

dest = (N-1, M-1)

def bfs(st, ds):
    q = deque()
    q.append(st)
    visited = [[0] * M for _ in range(N)]
    visited[st[0]][st[1]] = 1
    
    nexts = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        now = q.popleft()
        for nxt in nexts:
            i = now[0] + nxt[0]
            j = now[1] + nxt[1]
            if i >= 0 and i < N and j >= 0 and j < M:
                if board[i][j] != 0 and visited[i][j] == 0:
                    visited[i][j] = visited[now[0]][now[1]] + 1
                    q.append((i, j))
    return visited

visited = bfs(start, dest)

print(visited[N-1][M-1])