import sys
import math

input = sys.stdin.readline

n = int(input())
m = int(input())

# n = 5
# m = 14
# inputs = [[1, 2, 2],
# [1, 3, 3], 
# [1, 4, 1],
# [1, 5, 10],
# [2, 4, 2],
# [3, 4, 1],
# [3, 5, 1],
# [4, 5, 3],
# [3, 5, 10],
# [3, 1, 8],
# [1, 4, 2],
# [5, 1, 7],
# [3, 4, 2],
# [5, 2, 4]]

distance = [[math.inf for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    distance[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    # [a, b, c] = inputs[i]
    if distance[a][b] > c:
        distance[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            # if j == k:
            #     continue
            distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])

# print(distance)

for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] == math.inf:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()