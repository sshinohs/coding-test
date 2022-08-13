import sys
from collections import deque
import math

input = sys.stdin.readline

st, des = map(int, input().split())

limit_min = 0
limit_max = 100000


def bfs(st, des):

    q = deque()

    distances = [math.inf] * 100001

    flag = False

    distances[st] = 0

    route_num = 0

    q.append((st, 0))

    while q:
        now, dist = q.popleft()
        if now == des:
            flag = True
        
        if flag:
            if distances[now] > distances[des]:
                break

        if distances[now] == dist:
            if now == des:
                route_num += 1
        
        nxt_pos = [now - 1, now + 1, now * 2]
        for nxt in nxt_pos:
            if nxt >= limit_min and nxt <= limit_max:
                if distances[nxt] >= distances[now] + 1:
                    distances[nxt] = distances[now] + 1
                    q.append((nxt, distances[nxt]))
    return distances[des], route_num

min_time, count = bfs(st, des)
print(min_time)
print(count)
