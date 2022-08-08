from collections import defaultdict
def solution(arrows):
    parents = defaultdict(int)
    steps = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    now = (0, 0)
    parents[now] = (0, 0)
    answer = 0
    for arrow in arrows:
        nxt = (now[0] + steps[arrow][0], now[1] + steps[arrow][1])
        if parents[nxt] == 0:
            parents[nxt] = nxt
        elif find_parents(parents, now) == find_parents(parents, nxt):
            answer += 1
        unify(parents, now, nxt)
        now = nxt
            
    return answer

def unify(parents, a, b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)
    if a != b:
        if abs(a[0]) < abs(b[0]):
            parents[b] = a
        elif abs(b[0]) < abs(a[0]):
            parents[a] = b
        elif abs(a[0]) == abs(b[0]):
            if a[0] > b[0]:
                parents[b] = a
            elif b[0] > a[0]:
                parents[a] = b
            elif a[0] == b[0]:
                if abs(a[1]) < abs(b[1]):
                    parents[b] = a
                elif abs(b[1]) < abs(a[1]):
                    parents[a] = b
                elif abs(a[1]) == abs(b[1]):
                    if a[1] > b[1]:
                        parents[b] = a
                    elif b[1] > a[1]:
                        parents[a] = b

def find_parents(parents, pos):
    if parents[pos] != pos:
        parents[pos] = parents[find_parents(parents, pos)]
    return parents[pos]


arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]

print(solution(arrows))