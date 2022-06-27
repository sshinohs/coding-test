import heapq
import sys

input = sys.stdin.readline

N = int(input())

h = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h, num)