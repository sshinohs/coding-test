import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

truth = [0] * (N+1)

know_people = map(int, input().split()[1:])

# for i in map(int, input().split()[1:]):
#     truth[i] = 1

edges = [[] for _ in range(N+1)]

party_arr = []
for _ in range(M):
    party = list(map(int, input().split()))
    for i in party[1:]:
        for j in party[1:]:
            if i != j:
                edges[i].append(j)
    party_arr.append(party[1:])

# print(edges)


def dfs(st):
    stack = deque()
    stack.append(st)
    
    while stack:
        now = stack.pop()
        if truth[now] == 0:
            truth[now] = 1
            for edge in edges[now]:
                stack.append(edge)

for i in know_people:
    # print(i)
    dfs(i)

count = 0

# print(party_arr)

for part in party_arr:
    flag = False
    for pa in part:
        if truth[pa]:
            flag = True
    if not flag:
        count += 1

print(count)