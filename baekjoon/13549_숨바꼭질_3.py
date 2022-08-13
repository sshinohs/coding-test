import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())


def bfs(st, des):
    if st >= des:
        return st-des
    q = deque()
    visited = [-1] * (100001)
    q.append(st)
    visited[st] = 0

    while q:
        now = q.popleft()
        count = 0
        nxt = now * 2 ** count
        while nxt <= 100000:
            visited[nxt] = visited[now]
            if nxt == des:
                return visited[nxt]
            else:
                if nxt > 0:
                    if visited[nxt - 1] == -1:
                        q.append(nxt - 1)
                        visited[nxt - 1] = visited[now] + 1
                if nxt < 100000:
                    if visited[nxt + 1] == -1:
                        q.append(nxt + 1)
                        visited[nxt + 1] = visited[now] + 1
                count += 1
                if nxt == 0:
                    break
                nxt = now * 2 ** count

print(bfs(N, K))