import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n, m = map(int, input().split())

parents = list(range(n+1))

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_nodes(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)

    if a <= b:
        parents[b] = a
    else:
        parents[a] = b

for _ in range(m):
    command, a, b = map(int, input().split())
    if command == 0:
        union_nodes(parents, a, b)
    elif command == 1:
        if find_parent(parents, a) == find_parent(parents, b):
            print('YES')
        else:
            print('NO')