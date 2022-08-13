import sys

input = sys.stdin.readline

def find_num(ii, jj):

    if (ii, jj) == (0, 0):
        return 1

    group_num = max(abs(ii), abs(jj))

    base_num = ((group_num * 2) - 1) ** 2

    pos_i = group_num
    pos_j = group_num

    for _ in range(group_num*2):
        base_num += 1
        pos_i -= 1
        if (ii, jj) == (pos_i, pos_j):
            return base_num

    for _ in range(group_num*2):
        base_num += 1
        pos_j -= 1
        if (ii, jj) == (pos_i, pos_j):
            return base_num

    for _ in range(group_num*2):
        base_num += 1
        pos_i += 1
        if (ii, jj) == (pos_i, pos_j):
            return base_num

    for _ in range(group_num*2):
        base_num += 1
        pos_j += 1
        if (ii, jj) == (pos_i, pos_j):
            return base_num


r1, c1, r2, c2 = map(int, input().split())

board = []
for i in range(r1, r2+1):
    row = []
    for j in range(c1, c2+1):
        row.append(find_num(i, j))
    board.append(row)



max_len = len(str(max(map(max, board))))
padding = ' '

for row in board:
    flag = False
    for num in row:
        str_num = str(num)
        if flag:
            print(f'{str_num : >{max_len+1}}', end='')
        else:
            print(f'{str_num : >{max_len}}', end='')
        flag = True
    print()