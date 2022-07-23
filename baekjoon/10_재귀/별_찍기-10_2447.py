import sys

input = sys.stdin.readline

N = int(input())

board = [[1] * N for _ in range(N)]

def recur_func(board, i0, j0, N):
    for i in range(i0 + N//3*1, i0 + N//3*2):
        for j in range(j0 + N//3*1, j0 + N//3*2):
            board[i][j] = 0
    if N > 3:
        for nxi in range(3):
            for nxj in range(3):
                if nxi != 1 or nxj != 1:
                    recur_func(board, i0+N//3*nxi, j0+N//3*nxj, N//3)


recur_func(board, 0, 0, N)

for row in board:
    for element in row:
        if element == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()