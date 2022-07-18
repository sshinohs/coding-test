from collections import deque

def solution(n, edge):
    edges = [[] for _ in range(n+1)]
    for ed in edge:
        a = ed[0]
        b = ed[1]
        edges[a].append(b)
        edges[b].append(a)
    
    result_arr = bfs(n, edges, 1)
    far_num = max(result_arr)
    answer = result_arr.count(far_num)
    return answer

def bfs(n, edges, st):
    visited = [0] * (n+1)
    q = deque()
    q.append(st)
    visited[st] = 1
    
    while q:
        now = q.popleft()
        for edge in edges[now]:
            if visited[edge] == 0:
                visited[edge] = visited[now] + 1
                q.append(edge)
    return visited
        

