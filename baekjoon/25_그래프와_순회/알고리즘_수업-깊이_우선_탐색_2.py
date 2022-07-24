import sys
# from collections import deque

[N, M, R] = list(map(int, sys.stdin.readline().split()))

links = [[] for _ in range(N+1)]

for _ in range(M):
    [a, b] = list(map(int, sys.stdin.readline().split()))
    links[a].append(b)
    links[b].append(a)

visited = [0] * (N+1)

# queue = deque()
stack = []

# visited[R] = 1
stack.append(R)

count = 0

output = [0] * N

for i in range(N+1):
    links[i].sort()

while stack:
    cur = stack.pop()

    if visited[cur] != 0:
        continue
    visited[cur] = 1
    count += 1

    output[cur-1] = count

    for des in links[cur]:
        if visited[des] == 0:
            # visited[des] = 1
            stack.append(des)

print(*output, sep="\n")