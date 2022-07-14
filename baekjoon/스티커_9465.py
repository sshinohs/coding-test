import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    board = []
    board.append(list(map(int, input().split())))
    board.append(list(map(int, input().split())))

    cumul_board = []
    cumul_board.append([0] * (n+2))
    cumul_board.append([0] * (n+2))
    
    for i in range(len(board[0])):
        cumul_board[0][i+2] = max(cumul_board[1][i+1], cumul_board[0][i], cumul_board[1][i]) + board[0][i]
        cumul_board[1][i+2] = max(cumul_board[0][i+1], cumul_board[0][i], cumul_board[1][i]) + board[1][i]
    
    print(max(cumul_board[0][-1], cumul_board[1][-1]))