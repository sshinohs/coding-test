import sys
import heapq

input = sys.stdin.readline

N = int(input())
K = int(input())

links = [[] for _ in range(N+1)]
for _ in range(K):
    a, b = map(int, input().split())
    links[a].append(b)
    links[b].append(a)

infected = [0 for _ in range(N+1)]

def bfs():
    
    h = []
    
    heapq.heappush(h, 1)
    infected[1] = 1

    while h:
        now = heapq.heappop(h)
        
        for link in links[now]:
            if infected[link] == 0:
                heapq.heappush(h, link)
                infected[link] = 1

bfs()

# print(infected)
print(sum(infected)-1)
