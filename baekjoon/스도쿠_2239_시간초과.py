# 시간 초과 이유, 딥카피

import sys
import copy
from collections import deque

input = sys.stdin.readline

N = 9

board = []
for _ in range(N):
    board.append(list(map(int, list(input().strip()))))

column_nums = [list(range(1, 10)) for _ in range(N)]
row_nums = [list(range(1, 10)) for _ in range(N)]
block_nums = [[list(range(1, 10)) for _ in range(N//3)] for _ in range(N//3)]

for i in range(N):
    for j in range(N):
        if board[i][j] in column_nums[j]:
            column_nums[j].remove(board[i][j])
        if board[i][j] in row_nums[i]:
            row_nums[i].remove(board[i][j])
        if board[i][j] in block_nums[i//3][j//3]:
            
            block_nums[i//3][j//3].remove(board[i][j])

def dfs(board, N, block_nums, column_nums, row_nums):
    st = 0
    i = st // N
    j = st % N
    stack = deque()

    stack.append([copy.deepcopy(board), st, copy.deepcopy(block_nums), copy.deepcopy(column_nums), copy.deepcopy(row_nums)])
    
    while stack:
        now_board, now, nb, nc, nr = stack.pop()
        i = now // N
        j = now % N

        if now == N**2-1 and now_board[i][j] != 0:
            
            return nb, nc, nr, now_board
        if board[i][j] == 0:
            num_candidate = list(set(nb[i//3][j//3]) & set(nc[j]) & set(nr[i]))
            num_candidate.sort(reverse=True)
            for num in num_candidate:
                nb_nxt = copy.deepcopy(nb)
                nc_nxt = copy.deepcopy(nc)
                nr_nxt = copy.deepcopy(nr)
                nxt_board = copy.deepcopy(now_board)
                
                nb_nxt[i//3][j//3].remove(num)
                nc_nxt[j].remove(num)
                nr_nxt[i].remove(num)
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