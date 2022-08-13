import sys

input = sys.stdin.readline

N = int(input())

board = [0] * (10001)


for _ in range(N):
    num = int(input())
    board[num] += 1

for i, count in enumerate(board):
    for _ in range(count):
        print(i)