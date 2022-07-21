def solution(n, costs):
    roots = [i for i in range(n+1)]
    costs.sort(key = lambda x : x[2])
    
    total_cost = 0
    for edge in costs:
        if not find_root(roots, edge[0]) == find_root(roots, edge[1]):
            total_cost += edge[2]
            island_union(roots, edge[0], edge[1])
    
    answer = total_cost
    return answer


def find_root(roots, x):
    if roots[x] != x:
        roots[x] = find_root(roots, roots[x])
    return roots[x]

def island_union(roots, a, b):
    a = find_root(roots, a)
    b = find_root(roots, b)
    
    if a <= b:
        roots[b] = a
    else:
        roots[a] = b