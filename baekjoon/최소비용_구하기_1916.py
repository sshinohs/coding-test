import sys
import heapq
import math

input = sys.stdin.readline

N = int(input())

M = int(input())

edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))

A, B = map(int, input().split())

def dijkstra(edges, st, ed):
    h = []
    distance = [math.inf] * (N+1)

    heapq.heappush(h, (0, st))

    while h:
        dist, now = heapq.heappop(h)
        distance[now] = dist

        if now == ed:
            return distance[now]
        
        for edge in edges[now]:
            if distance[edge[0]] > dist + edge[1]:
                distance[edge[0]] = dist + edge[1]
                heapq.heappush(h, (dist + edge[1], edge[0]))

print(dijkstra(edges, A, B))