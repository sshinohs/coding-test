import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

gems = []

for _ in range(N):
    heapq.heappush(gems, tuple(map(int, input().split())))

knapsacks = []

for _ in range(K):
    heapq.heappush(knapsacks, int(input()))

candidates = []

count = 0

while knapsacks:
    sack = heapq.heappop(knapsacks)
    
    while gems:
        if gems[0][0] <= sack:
            heapq.heappush(candidates, -gems[0][1])
            heapq.heappop(gems)
        else:
            break
    
    if candidates:
        count -= heapq.heappop(candidates)
    elif not gems:
        break

print(count)
    