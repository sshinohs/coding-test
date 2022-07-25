import sys

input = sys.stdin.readline

N = int(input())

board = list(map(int, input().split()))

# print(board)

cumul = [0] * (N)

# print('%%')
for i, num in enumerate(board):
    best = 0
    for j in range(i-1, -1, -1):
        if board[i] > board[j] and best < cumul[j]:
            best = cumul[j]
    cumul[i] = best + 1
print(board)
print(cumul)
print(max(cumul))