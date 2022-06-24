import sys
import math
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())

start = int(input())

links = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    links[u].append((v, w))

# print(links)

distance = [math.inf] * (V + 1)

distance[start] = 0

q = []

heapq.heappush(q, (0, start))

while q:
    # print(distance)
    dist, now = heapq.heappop(q)
    
    if distance[now] < dist:
        continue
    
    # distance[now] = dist
    
    for line in links[now]:
        # print(now)
        # print(line)
        cost = distance[now] + line[1]
        if distance[line[0]] > cost:
            distance[line[0]] = cost
            heapq.heappush(q, (cost, line[0]))

for i in range(1, len(distance)):
    if distance[i] == math.inf:
        print('INF')
    else:
        print(distance[i])