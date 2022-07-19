import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    board = [[0]*3 for _ in range(n+1)]

    for i, num in enumerate(map(int, input().split())):
        if board[num][0] == 0 or (i - board[num][2])%2 == 1:
            board[num][2] = i
            board[num][1] += 1
            if board[num][0] < board[num][1]:
                board[num][0] = board[num][1]
        else:
            board[num][2] = i
            board[num][1] = 1
    
    for boa in board[1:]:
        print(boa[0], end=' ')
    print()