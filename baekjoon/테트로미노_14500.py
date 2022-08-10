import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

diff = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def fu(board, N, M, diff, pos):

    global max_count

    for i in range(4):
        count = board[pos[0]][pos[1]]
        for j in range(4):
            if j != i:
                nxt = (pos[0] + diff[j][0], pos[1] + diff[j][1])
                if nxt[0] >= 0 and nxt[0] < N and nxt[1] >= 0 and nxt[1] < M:
                    count += board[nxt[0]][nxt[1]]
        if max_count < count:
            max_count = count
            
    

def dfs(board, N, M, diff, pos, count, num):

    global max_count

    count += board[pos[0]][pos[1]]
    num += 1

    if num == 4:
        if max_count < count:
            max_count = count
    else:
        for dif in diff:
            nxt_pos = (pos[0] + dif[0], pos[1] + dif[1])
            if nxt_pos[0] >= 0 and nxt_pos[0] < N and nxt_pos[1] >= 0 and nxt_pos[1] < M:
                temp = board[pos[0]][pos[1]]
                if board[nxt_pos[0]][nxt_pos[1]] != 0:
                    board[pos[0]][pos[1]] = 0
                    dfs(board, N, M, diff, nxt_pos, count, num)
                    board[pos[0]][pos[1]] = temp


total_max = 0

global max_count

for i in range(N):
    for j in range(M):
        max_count = 0
        check = dfs(board, N, M, diff, (i, j), 0, 0)
        if total_max < max_count:
            total_max  = max_count
        
        max_count = 0
        check = fu(board, N, M, diff, (i, j))
        if total_max < max_count:
            total_max  = max_count

print(total_max)