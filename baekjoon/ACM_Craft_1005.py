import sys
from collections import deque
import copy

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    N, K = map(int, input().split())

    indegree = [0] * (N+1)

    edges = [[] for _ in range(N+1)]

    cost = [0] + list(map(int, input().split()))

    # cumul_cost = [0] * (N+1)
    # visited = [0] * (N+1)

    for _ in range(K):
        a, b = map(int, input().split())
        edges[a].append(b)
        indegree[b] += 1

    W = int(input())

    def topology_sort(w):
        result = copy.deepcopy(cost)
        q = deque()

        for i in range(1, N + 1):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            now = q.popleft()

            for i in edges[now]:
                result[i] = max(result[i], result[now] + cost[i])
                indegree[i] -= 1
                
                if indegree[i] == 0:
                    q.append(i)
        
        print(result[w])

    topology_sort(W)

