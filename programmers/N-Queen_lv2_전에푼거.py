def solution(n):
    board = [[1 for i in range(n)] for i in range(n)]
    position = []
    answer = number_available(board)
    return answer

def number_available(board):
    count = 0
    
    if sum(board[0]) == 0:
        return count
    
    if len(board) == 1:
        for i in board[0]:
            if i == 1:
                count += 1
        return count
    else:
        for i, val in enumerate(board[0]):
            if val == 1:
                under_board = board_maker(board, i)
                count += number_available(under_board)
    return count

def board_maker(board, n):
    new_board = copy_cut_arr(board)
    for i in range(len(new_board)):
        for j in range(len(new_board[0])):
            if isDanger(n, i+1, j):
                new_board[i][j] = 0
    return new_board

def isDanger(n, i, j):
    if (n-j) == 0:
        return True
    elif abs(i/(n-j)) == 1:
        return True
    else:
        return False

def copy_cut_arr(arr):
    new_arr = []
    for i in range(1, len(arr)):
        new_arr.append(arr[i][:])
    return new_arr