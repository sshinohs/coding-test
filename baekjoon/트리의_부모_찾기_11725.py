import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

edges = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

parents = [0] * (N + 1)

visited = [0] * (N + 1)

root = 1

def dfs(st):
    q = deque()
    q.append(st)
    while q:
        now = q.pop()
        # print(now)
        # print(parents)
        if visited[now] == 0:
            visited[now] = 1
            for edge in edges[now]:
                if parents[edge] == 0:
                    parents[edge] = now
                    q.append(edge)
    

dfs(root)

for i in parents[2:]:
    print(i)