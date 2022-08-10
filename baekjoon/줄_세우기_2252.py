import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

remain = [0] * (N+1)

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    remain[b] += 1
    graph[a].append(b)

h = []

for i in range(1, N+1):
    if remain[i] == 0:
        heapq.heappush(h, i)

while h:
    now = heapq.heappop(h)
    print(now, end=' ')
    
    for edge in graph[now]:
        remain[edge] -= 1
        if remain[edge] == 0:
            heapq.heappush(h, edge)
