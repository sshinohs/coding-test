import sys
import heapq
import math

input = sys.stdin.readline

N, M, X = map(int, input().split())

edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    edges[a].append((cost, b))

def dijkstra(edges, st, des):
    distance = [math.inf for _ in range(N+1)]
    hq = []
    distance[st] = 0
    for edge in edges[st]:
        if distance[edge[1]] > distance[st] + edge[0]:
            distance[edge[1]] = distance[st] + edge[0]
            heapq.heappush(hq, edge)
    
    while hq:
        now = heapq.heappop(hq)
        if now[1] == des:
            return distance[now[1]]
        for edge in edges[now[1]]:
            if distance[edge[1]] > distance[now[1]] + edge[0]:
                distance[edge[1]] = distance[now[1]] + edge[0]
                heapq.heappush(hq, (distance[edge[1]], edge[1]))

max_count = 0
for i in range(1, N+1):
    if i != X:
        check = dijkstra(edges, i, X) + dijkstra(edges, X, i)
        if  max_count < check:
            max_count = check

print(max_count)