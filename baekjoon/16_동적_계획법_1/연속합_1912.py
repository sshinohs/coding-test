import sys
import math

input = sys.stdin.readline

n = int(input())

cumul = [(-math.inf, -math.inf)]

for i in map(int, input().split()):
    if cumul[-1][0] > 0:
        a = cumul[-1][0] + i
    else:
        a = i
    b = max(cumul[-1][1], a)
    cumul.append((a, b))

print(cumul[-1][1])