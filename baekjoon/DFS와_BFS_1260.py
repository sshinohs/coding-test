import sys
from collections import deque

def dfs(st):
    visited = [0] * (N + 1)
    stack = deque()
    stack.append(st)

    while stack:
        now = stack.pop()
        
        if visited[now] == 0:
            visited[now] = 1
            print(now, end=' ')
            for edge in edges[now][::-1]:
                stack.append(edge)


def bfs(st):
    visited = [0] * (N + 1)
    q = deque()
    q.append(st)
    visited[st] = 1

    while q:
        now = q.popleft()
        print(now, end= ' ')
        for edge in edges[now]:
            if visited[edge] == 0:
                q.append(edge)
                visited[edge] = 1



input = sys.stdin.readline

N, M, V = map(int, input().split())

edges = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

for i in range(N+1):
    edges[i] = sorted(edges[i])


dfs(V)
print()
bfs(V)