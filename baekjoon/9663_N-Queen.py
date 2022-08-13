import sys

input = sys.stdin.readline

N = int(input())

count = 0

board = [[1] * N for _ in range(N)]

# print(board)

def nqueen(board):
    # print('%%')
    # for row in board:
    #     print(row)
    # print('##')
    if len(board) == 1:
        return sum(board[0])
    if sum(board[0]) == 0:
        return 0
    count = 0
    for check_j, check in enumerate(board[0]):
        if check:
            board_sub = []
            for row in board[1:]:
                board_sub.append(row[:])
            for i in range(len(board_sub)):
                for j in range(len(board_sub[0])):
                    if j == check_j or abs(j-check_j) == (i+1):
                        board_sub[i][j] = 0
            count += nqueen(board_sub)
    return count

print(nqueen(board))