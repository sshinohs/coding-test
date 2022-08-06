import sys
import copy

input = sys.stdin.readline

N = int(input())

max_board = list(map(int, input().split()))
min_board = copy.deepcopy(max_board)

for _ in range(N-1):
    a, b, c = map(int, input().split())
    a_nxt = max(max_board[0], max_board[1]) + a
    b_nxt = max(max_board) + b
    c_nxt = max(max_board[1], max_board[2]) + c
    max_board = [a_nxt, b_nxt, c_nxt]

    a_nxt = min(min_board[0], min_board[1]) + a
    b_nxt = min(min_board) + b
    c_nxt = min(min_board[1], min_board[2]) + c
    min_board = [a_nxt, b_nxt, c_nxt]

print(max(max_board), min(min_board))