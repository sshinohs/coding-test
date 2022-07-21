# import sys
# import math

# input = sys.stdin.readline

# N = int(input())

# dp = [[math.inf]*(1 << N) for _ in range(N)]

# def dfs(x, visited):
#     if visited == (1 << N) - 1:
#         if graph[x][0]:
#             return graph[x][0]
#         else:
#             return math.inf
    
#     if dp[x][visited] != math.inf:
#         return dp[x][visited]
    
#     for i in range(1, N):
#         if not graph[x][i]:
#             continue
#         if visited & (1 << i):
#             continue

#         dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1<<i)) + graph[x][i])
#     return dp[x][visited]

# graph = []
# for i in range(N):
#     graph.append(list(map(int, input().split())))

# print(dfs(0, 1))

import sys
N = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * (1 << N - 1) for _ in range(N)]

def solution(i, route):
    print('i:', i, 'route(2진수):', bin(route), 'route:', route)
    print(dp)
    print()
    if dp[i][route] != 0:
        return dp[i][route]

    if route == (1 << (N - 1)) - 1:
        print('ho')
        if W[i][0]:
            return W[i][0]
        else:
            return float('inf')
            
    min_dist = float('inf')
    for j in range(1, N):
        if not W[i][j]:
            continue
        if route & (1 << j - 1):
            continue
        dist = W[i][j] + solution(j, route | (1 << (j - 1)))
        if min_dist > dist:
            min_dist = dist
    dp[i][route] = min_dist
    
    return min_dist

print(solution(0, 0))