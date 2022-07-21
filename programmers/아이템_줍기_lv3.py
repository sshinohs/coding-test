from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    max_len = 100
    board = [[1] * (max_len + 1) for _ in range(max_len + 1)]
    
    for rectan in rectangle:
        rectan = list(map(x2, rectan))
        for i in range(rectan[0], rectan[2]+1):
            for j in range(rectan[1], rectan[3]+1):
                board[i][j] = 0
    
    for rectan in rectangle:
        rectan = list(map(x2, rectan))
        for i in range(rectan[0]+1, rectan[2]):
            for j in range(rectan[1]+1, rectan[3]):
                board[i][j] = 1
    answer = bfs(board, (characterX*2, characterY*2), (itemX*2, itemY*2))
    return answer

def x2(x):
    return x*2

def bfs(board, st, des):
    len_board = (len(board), len(board[0]))
    q = deque()
    diff = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q.append(st)
    board[st[0]][st[1]] = 1
    while q:
        now = q.popleft()
        if now == des:
            return board[now[0]][now[1]]//2
        for dif in diff:
            nxt = (now[0] + dif[0], now[1] + dif[1])
            if nxt[0] > 0 and nxt[0] < len_board[0] and nxt[1] > 0 and nxt[1] < len_board[1]:
                if board[nxt[0]][nxt[1]] == 0:
                    board[nxt[0]][nxt[1]] = board[now[0]][now[1]] + 1
                    q.append(nxt)
    