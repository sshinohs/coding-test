import sys

input = sys.stdin.readline

total_num = 10001

board = [[0]*(total_num) for _ in range(total_num)]

count = 1

pos_i = 5000
pos_j = 5000

board[pos_i][pos_j] = 1

line_len = 1

while count < total_num**2:
    pos_j += 1
    count += 1
    board[pos_i][pos_j] = count
    for _ in range(2*line_len-1):
        count += 1
        pos_i -= 1
        board[pos_i][pos_j] = count
    for _ in range(2*line_len):
        count += 1
        pos_j -= 1
        board[pos_i][pos_j] = count
    for _ in range(2*line_len):
        count += 1
        pos_i += 1
        board[pos_i][pos_j] = count
    for _ in range(2*line_len):
        count += 1
        pos_j += 1
        board[pos_i][pos_j] = count

    line_len += 1

print('ho')
r1, c1, r2, c2 = map(int, input().split())

for i in range(r1+5000, r2+5000+1):
    for j in range(c1+5000, c2+5000+1):
        print(board[i][j], end=' ')
    print()