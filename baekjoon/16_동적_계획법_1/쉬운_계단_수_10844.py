import sys

input = sys.stdin.readline

N_max = 100

board = [[0] * 12 for _ in range(N_max + 1)]

board[1] = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

N = int(input())

for i in range(2, N+1):
    for j in range(1, 11):
        board[i][j] = board[i-1][j-1] + board[i-1][j+1]

print(sum(board[N])%1000000000)
        