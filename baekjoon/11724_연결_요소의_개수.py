import sys

def dfs(start):
    stack = []
    stack.append(start)
    
    while stack:
        now = stack.pop()
        visited[now] = 1
        
        for nt in links[now]:
            if visited[nt] == 0:
                stack.append(nt)


input = sys.stdin.readline

N, M = map(int, input().split())

links = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    links[a].append(b)
    links[b].append(a)

visited = [0] * (N+1)

visited[0] = 1

count = 0

# print(visited)

while sum(visited) < N+1:
    for i in range(N+1):
        if visited[i] == 0:
            count += 1
            dfs(i)
            break

print(count)