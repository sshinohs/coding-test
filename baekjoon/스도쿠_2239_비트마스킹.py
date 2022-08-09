# 시간 초과 이유, 딥카피

import sys
import copy
from collections import deque

input = sys.stdin.readline

N = 9

board = []
for _ in range(N):
    board.append(list(map(int, list(input().strip()))))

column_nums = [[1]*(N+1) for _ in range(N)]
row_nums = [[1]*(N+1) for _ in range(N)]
block_nums = [[[1]*(N+1) for _ in range(N//3)] for _ in range(N//3)]

for i in range(N):
    for j in range(N):
        column_nums[j][board[i][j]] = 0
        row_nums[i][board[i][j]] = 0
        block_nums[i//3][j//3][board[i][j]] = 0

def dfs(board, N, block_nums, column_nums, row_nums):
    st = 0
    stack = deque()

    stack.append([copy.deepcopy(board), st, copy.deepcopy(block_nums), copy.deepcopy(column_nums), copy.deepcopy(row_nums)])
    
    while stack:
        now_board, now, nb, nc, nr = stack.pop()
        i = now // N
        j = now % N

        if now == N**2-1 and now_board[i][j] != 0:
            return nb, nc, nr, now_board
        if board[i][j] == 0:
            for num in range(9, 0, -1):
                if nb[i//3][j//3][num] and nc[j][num] and nr[i][num]:
                    nb_nxt = copy.deepcopy(nb)
                    nc_nxt = copy.deepcopy(nc)
                    nr_nxt = copy.deepcopy(nr)
                    nxt_board = copy.deepcopy(now_board)
                
                    nb_nxt[i//3][j//3][num] = 0
                    nc_nxt[j][num] = 0
                    nr_nxt[i][num] = 0
                    nxt_board[i][j] = num

                    if now == N**2-1:
                        return nb, nc, nr, nxt_board
                    stack.append([nxt_board, now+1, nb_nxt, nc_nxt, nr_nxt])
        else:
            stack.append([now_board, now+1, nb, nc, nr])
    
    return 'error'

nb, nc, nr, answer = dfs(board, N, block_nums, column_nums, row_nums)

for row in answer:
    for num in row:
        print(num, end='')
    print()