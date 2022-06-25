import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())

check = ['WBWBWBWB', 'BWBWBWBW']

min_count = math.inf

board = []
for _ in range(N):
    board.append(*input().split())

# print(board)

for i in range(N-7):
    for j in range(M-7):
        count = 0
        for row in range(8):
            for k, ch in enumerate(check[row%2]):
                if board[i+row][j+k] != ch:
                    count += 1
        if min_count > count:
            min_count = count

for i in range(N-7):
    for j in range(M-7):
        count = 0

        for row in range(8):

            for k, ch in enumerate(check[(row+1)%2]):
                if board[i+row][j+k] != ch:
                    count += 1

        if min_count > count:
            min_count = count
        
        
print(min_count)

