import sys
from collections import deque
import math

input = sys.stdin.readline

N, M = map(int, input().split())

edges = list(range(100 + 1))

for _ in range(N):
    a, b = map(int, input().split())
    edges[a] = b

for _ in range(M):
    a, b = map(int, input().split())
    edges[a] = b

def bfs(edges):
    st = 1
    q = deque()
    visited = [math.inf] * (100 + 1)
    visited[st] = 0
    q.append(st)

    while q:
        now = q.popleft()
        
        if now == 100:
            return visited[now]
        
        for dif in range(1,7):
            nxt = now + dif
            if nxt <= 100:
                if visited[nxt] > visited[now] + 1:
                    visited[nxt] = visited[now] + 1
                    if visited[edges[nxt]] >= visited[now] + 1:
                        visited[edges[nxt]] = visited[now] + 1
                        q.append(edges[nxt])

print(bfs(edges))
                