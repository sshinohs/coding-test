import heapq
import sys

input = sys.stdin.readline

N = int(input())

h = []

for _ in range(N):
    oper = int(input())
    if oper == 0:
        if h:
            output = heapq.heappop(h)
            print(output[1])
        else:
            print(0)
    else:
        heapq.heappush(h, (abs(oper), oper))