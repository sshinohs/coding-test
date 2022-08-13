import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

# print(board)

cumul_j = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        cumul_j[i][j] = cumul_j[i][j-1] + board[i-1][j-1]

# print(cumul_j)

cumul_ij = [[0] * (N+1) for _ in range(N+1)]

for j in range(1, N+1):
    for i in range(1, N+1):
        cumul_ij[i][j] = cumul_ij[i-1][j] + cumul_j[i][j]

for _ in range(M):
    i1, j1, i2, j2 = map(int, input().split())
    answer = cumul_ij[i2][j2] - cumul_ij[i1-1][j2] - cumul_ij[i2][j1-1] + cumul_ij[i1-1][j1-1]
    print(answer)
