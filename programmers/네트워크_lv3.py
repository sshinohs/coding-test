def solution(n, computers):
    roots = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                union_com(roots, i, j)

    for i in range(n):
        find_root(roots, i)

    result_set = set(roots)
    answer = len(result_set)
    return answer

def find_root(roots, x):
    if roots[x] == x:
        return x
    else:
        roots[x] = find_root(roots, roots[x])
    return roots[x]

def union_com(roots, a, b):
    a = find_root(roots, a)
    b = find_root(roots, b)

    if a <= b:
        roots[b] = a
    else:
        roots[a] = b