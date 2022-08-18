import copy
def solution(n):
    board = []
    for _ in range(n):
        board.append([1]*(n))
    answer = nqueens(board, n, 0)
    
    return answer

def nqueens(board, n, ii):
    if ii == n-1:
        return sum(board[0])
    count = 0
    for j in range(n):
        if board[0][j]:
            nxt_board = [row[:] for row in board[1:]]
            for i in range(n-ii-1):
                nxt_board[i][j] = 0
                if j+i+1 < n:
                    nxt_board[i][j+i+1] = 0
                if j-i-1 >= 0:
                    nxt_board[i][j-i-1] = 0
            count += nqueens(nxt_board, n, ii+1)
    return count