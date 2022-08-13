import sys
import math

INF = int(1e9)
input = sys.stdin.readline

def bellman_ford(start):

    distance = [INF for _ in range(N+1)]

    for i in range(N):
        for edge in edges:
            if distance[edge[1]] > distance[edge[0]] + edge[2]:
                distance[edge[1]] = distance[edge[0]] + edge[2]
                if i == N - 1:
                    return True
    
    return False

TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())

    edges = []
    
    for _ in range(M):
        a, b, cost = map(int, input().split())
        edges.append((a, b, cost))
        edges.append((b, a, cost))
    
    for _ in range(W):
        a, b, cost = map(int, input().split())
        edges.append((a, b, -cost))

    flag = bellman_ford(1)
    if flag:
        print('YES')
    else:
        print('NO')


