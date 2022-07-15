import sys

input = sys.stdin.readline

N = int(input())

board = []

for _ in range(N):
    board.append(list(map(int, list(input().strip()))))

def quad_tree(y1, y2, x1, x2):
    check_num = sum([sum(row[x1:x2]) for row in board[y1:y2]])
    if check_num == 0:
        return '0'
    elif check_num == (y2-y1) * (x2-x1):
        return '1'
    else:
        answer = '('
        quad_range_y = [(y1, y1 + (y2 - y1) // 2), (y1 + (y2 - y1) // 2, y2)]
        quad_range_x = [(x1, x1 + (x2 - x1) // 2), (x1 + (x2 - x1) // 2, x2)]
        for i in quad_range_y:
            for j in quad_range_x:
                answer += quad_tree(i[0], i[1], j[0], j[1])
        answer += ')'
        return answer

print(quad_tree(0, N, 0, N))