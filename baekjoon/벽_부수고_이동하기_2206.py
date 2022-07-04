import sys

input = sys.stdin.readline

# N, M = map(int, input().split())

N = 6
M = 4

# board = []

# for _ in range(N):
#     board.append(list(map(int, input()[:-1])))

board = [[0, -1, 0, 0], [-1, -1, -1, 0], [-1, 0, 0, 0], [0, 0, 0, 0], [0, -1, -1, -1], [0, 0, 0, 0]]

start = (0, 0)
dest = (N-1, M-1)

for i in range(N):
    for j in range(M):
        if board[i][j] == -1:
            board[i][j] = 0
            print(board)
            board[i][j] = -1
        




