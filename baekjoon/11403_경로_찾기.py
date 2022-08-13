import sys
import math

input = sys.stdin.readline

N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))


def floyd_warshall(arr, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                arr[i][j] = (arr[i][k] and arr[k][j]) or arr[i][j]

floyd_warshall(board, N)

for row in board:
    for num in row:
        print(num, end=' ')
    print()
