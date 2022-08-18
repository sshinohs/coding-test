import sys

input = sys.stdin.readline

board = []

N = 9

for _ in range(N):
    board.append(list(map(int, input().split())))

# for row in board:
#     print(row)

def sudoku(board, pos):
    if pos == N**2:
        return True
    
    ii = pos // N
    jj = pos % N

    if board[ii][jj] == 0:
        for num in range(1, N+1):
            flag = True
            for j in range(N):
                if board[ii][j] == num:
                    flag = False
                    break
            
            if flag:
                for i in range(N):
                    if board[i][jj] == num:
                        flag = False
                        break
            
            if flag:
                for i in range(ii//3*3, ii//3*3+3):
                    for j in range(jj//3*3, jj//3*3+3):
                        if board[i][j] == num:
                            flag = False
                            break
            
            if flag:
                board[ii][jj] = num
                if sudoku(board, pos+1):
                    return True
                board[ii][jj] = 0
    else:
        if sudoku(board, pos+1):
            return True

sudoku(board, 0)

for row in board:
    for num in row:
        print(num, end=' ')
    print()
    
        