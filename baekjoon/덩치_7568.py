import sys
import math

input = sys.stdin.readline

N = int(input())

profile = []
for i in range(N):
    profile.append(tuple(map(int, input().split())))

result = [math.inf] * N
for i in range(N):
    count = 1
    for j in range(N):
        if i != j:
            if profile[i][0] < profile[j][0] and profile[i][1] < profile[j][1]:
                count += 1
    # result[i] = count
    print(count, end=' ')

# print(result)