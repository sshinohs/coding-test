import heapq
import sys

input_num = int(sys.stdin.readline())

heap = []

for _ in range(input_num):
    num = int(sys.stdin.readline())

    if num == 0:
        if len(heap) != 0:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -num)


