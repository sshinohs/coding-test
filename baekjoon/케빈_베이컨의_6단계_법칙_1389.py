import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())

distance_arr = [[math.inf] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    distance_arr[i][i] = 0

# for i in distance_arr:
#     print(i)

for _ in range(M):
    a, b = map(int, input().split())
    distance_arr[a][b] = 1
    distance_arr[b][a] = 1

# for i in distance_arr:
#     print(i)


def floyd_warshall(n):
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                distance_arr[i][j] = min(distance_arr[i][j], distance_arr[i][k] + distance_arr[k][j])

floyd_warshall(N)

result = [math.inf] * (N+1)

for i, row in enumerate(distance_arr):
    result[i] = sum(row[1:])

# print(result)

# print('답')
print(result[1:].index(min(result[1:]))+1)