import sys
import heapq

num_cases = int(sys.stdin.readline())

for _ in range(num_cases):
    heap = []
    num_chapter = int(sys.stdin.readline())
    sizes_chapter = list(map(int, sys.stdin.readline().split()))
    count = 0

    for size in sizes_chapter:
        heapq.heappush(heap, size)
    
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        sum = a + b
        count += sum
        heapq.heappush(heap, sum)
    
    print(count)