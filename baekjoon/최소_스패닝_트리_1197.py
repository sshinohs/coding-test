import sys

input = sys.stdin.readline

V, E = map(int, input().split())

roots = [i for i in range(V+1)]

def find_root(x):
    if roots[x] != x:
        roots[x] = find_root(roots[x])
    return roots[x]


def union_nodes(a, b):
    a = find_root(a)
    b = find_root(b)

    if ap <= bp:
        roots[b] = a
    else:
        roots[a] = b

edges = []
for _ in range(E):
    edges.append(tuple(map(int, input().split())))

edges.sort(key = lambda x : x[2])

count = 0
for edge in edges:
    ap = find_root(edge[0])
    bp = find_root(edge[1])
    if ap != bp:
        count += edge[2]
        union_nodes(edge[0], edge[1])

print(count)