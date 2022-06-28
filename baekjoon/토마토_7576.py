import sys
from collections import deque


def bfs():
    q = deque()
    for i, pos_init in enumerate(mature):
        q.append(pos_init)
    
    while q:
        now = q.popleft()
        if now[0] > 0:
            if tomato[now[0]-1][now[1]] == 0:
                tomato[now[0]-1][now[1]] = tomato[now[0]][now[1]] + 1
                q.append((now[0]-1, now[1]))
        if now[0] < N-1:
            if tomato[now[0]+1][now[1]] == 0:
                tomato[now[0]+1][now[1]] = tomato[now[0]][now[1]] + 1
                q.append((now[0]+1, now[1]))
        if now[1] > 0:
            if tomato[now[0]][now[1]-1] == 0:
                tomato[now[0]][now[1]-1] = tomato[now[0]][now[1]] + 1
                q.append((now[0], now[1]-1))
        if now[1] < M-1:
            if tomato[now[0]][now[1]+1] == 0:
                tomato[now[0]][now[1]+1] = tomato[now[0]][now[1]] + 1
                q.append((now[0], now[1]+1))


input = sys.stdin.readline

M, N = map(int, input().split())

tomato = []
mature = []

# M = 11
# N = 11

# tomato = [[0, 0, 0, 0, 1, 0, -1, -1, 0, 0, 0], 
# [0, -1, 1, 1, 0, 0, 1, 1, 0, 0, 0], 
# [0, 0, 0, 0, -1, 1, 0, 0, 1, 0, 0], 
# [0, 0, -1, 0, 0, -1, -1, 0, 0, 0, -1], 
# [1, 1, -1, 0, 0, 1, 0, 0, 0, -1, 1], 
# [-1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
# [0, 1, 0, -1, 0, 0, 0, 0, 1, 1, 1],
# [0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
# [-1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
# [-1, 0, 0, 0, 0, -1, -1, 0, 0, 0, -1]]

for i in range(N):
    toma_row = []
    for j, toma in enumerate(map(int, input().split())):
        toma_row.append(toma)
        if toma == 1:
            mature.append((i, j))
    tomato.append(toma_row)

for i in range(N):
    for j, toma in enumerate(tomato[i]):
        if toma == 1:
            mature.append((i, j))

# print(mature)

bfs()


# print('%%')
# for toma in tomato:
#     print(toma)


flag = False
count = 0
for toma in tomato:
    for val in toma:
        if val == 0:
            flag = True
        if val > count:
            count = val

if flag:
    print(-1)
else:
    print(count - 1)