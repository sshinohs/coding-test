import sys
from collections import deque

input = sys.stdin.readline

def oper_D(n):
    answer = n * 2
    if answer > 9999:
        answer %= 10000
    return answer

def oper_S(n):
    answer = n - 1
    if answer == -1:
        answer = 9999
    return answer

def oper_L(n):
    temp = n % 10**3
    return temp * 10 + n // 10**3

def oper_R(n):
    temp = n // 10
    return temp + n % 10 * 10**3

def bfs_record(st, ed):
    visited = [0] * 10000
    q = deque()
    q.append([st, ''])
    visited[st] = 1

    while q:
        now, now_record = q.popleft()
        if now == ed:
            return now_record
        nxt_D = oper_D(now)
        if visited[nxt_D] == 0:
            visited[nxt_D] = 1
            q.append([nxt_D, now_record + 'D'])
        nxt_S = oper_S(now)
        if visited[nxt_S] == 0:
            visited[nxt_S] = 1
            q.append([nxt_S, now_record + 'S'])
        nxt_L = oper_L(now)
        if visited[nxt_L] == 0:
            visited[nxt_L] = 1
            q.append([nxt_L, now_record + 'L'])
        nxt_R = oper_R(now)
        if visited[nxt_R] == 0:
            visited[nxt_R] = 1
            q.append([nxt_R, now_record + 'R'])

T = int(input())

for _ in range(T):
    st, ed = map(int, input().split())
    print(bfs_record(st, ed))