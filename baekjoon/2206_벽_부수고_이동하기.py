import sys
from collections import deque

input = sys.stdin.readline

def bfs_one_break(visited, N, M):
    start = (0, 0, 0)
    dest = (N-1, M-1)

    neighbor_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    q = deque()

    q.append(start)

    while q:
        now = q.popleft()
        if now[:2] == dest[:2]:
            return visited[now[0]][now[1]][now[2]]
        for neighbor in neighbor_list:
            a = now[0]+neighbor[0]
            b = now[1]+neighbor[1]
            if a >= 0 and a < N and b >= 0 and b < M:
                if board[a][b] == 1 and now[2] == 0:
                    visited[a][b][1] = visited[now[0]][now[1]][0] + 1
                    q.append((a, b, 1))
                elif board[a][b] == 0 and visited[a][b][now[2]] == 0:
                    visited[a][b][now[2]] = visited[now[0]][now[1]][now[2]] + 1
                    q.append((a, b, now[2]))
    else:
        return -1


N, M = map(int, input().split())

def minus_int(x):
    return -int(x)

board = []

for _ in range(N):
    board.append(list(map(int, input()[:-1])))

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

visited[0][0][0] = 1

answer = bfs_one_break(visited, N, M)

# print(board)

print(answer)