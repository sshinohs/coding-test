import sys
import math
import heapq

input = sys.stdin.readline

N, E = map(int, input().split())

links = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    links[a].append((b, c))
    links[b].append((a, c))

v1, v2 = map(int, input().split())

via = [1, v1, v2]

def dijkstra(start):
    distance = [math.inf for _ in range(N+1)]
    distance[start] = 0

    q = []

    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for line in links[now]:
            cost = distance[now] + line[1]
            if distance[line[0]] > cost:
                distance[line[0]] = cost
                heapq.heappush(q, (cost, line[0]))
    
    return distance

results = []

for st in via:
    results.append(dijkstra(st))

answer1 = results[0][v1] + results[1][v2] + results[2][N]
answer2 = results[0][v2] + results[2][v1] + results[1][N]

answer = min(answer1, answer2)

if answer == math.inf:
    print(-1)
else:
    print(answer)
