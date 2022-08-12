import sys
import heapq
import math

input = sys.stdin.readline

n = int(input())

m = int(input())

edges = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))

st, ed = map(int, input().split())

def dijkstra(st, des):
    distance = [math.inf] * (n+1)
    routes = [[] for _ in range(n+1)]
    h = []
    distance[st] = 0
    heapq.heappush(h, (0, 0, st))

    while h:
        now_cost, last_pos, now_pos = heapq.heappop(h)

        if len(routes[now_pos]) > 0:
            continue

        routes[now_pos] = routes[last_pos] + [now_pos]

        if now_pos == des:
            return now_cost, routes[now_pos]
        
        for edge in edges[now_pos]:
            nxt_cost = now_cost + edge[1]
            if distance[edge[0]] > nxt_cost:
                distance[edge[0]] = nxt_cost
                heapq.heappush(h, (nxt_cost, now_pos, edge[0]))

cost, route = dijkstra(st, ed)

print(cost)
print(len(route))
for rou in route:
    print(rou, end=' ')
print()