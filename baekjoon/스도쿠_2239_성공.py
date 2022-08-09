import sys

input = sys.stdin.readline

N = 9

board = []
for _ in range(N):
    board.append(list(map(int, list(input().strip()))))

def dfs(pos):
    if pos == N**2:
        for row in board:
            for num in row:
                print(num, end='')
            print()
        return True

    i = pos // N
    j = pos % N
    
    if board[i][j] == 0:

        for num in range(1, 10):
            flag = True
            for ii in range(9):
                if board[ii][j] == num:
                    flag = False
            
            if flag:
                for jj in range(9):
                    if board[i][jj] == num:
                        flag = False
            
            if flag:
                for ii in range(i//3*3, i//3*3 + 3):
                    for jj in range(j//3*3, j//3*3 + 3):
                        if board[ii][jj] == num:
                            flag = False

            if flag:
                board[i][j] = num
                if dfs(pos+1):
                    return True
                board[i][j] = 0
    else:
        if dfs(pos+1):
            return True

dfs(0)