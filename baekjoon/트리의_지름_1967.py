import sys
input = sys.stdin.readline

def dfs(start):
    distance = [-1] * (n+1)
    # distance[start] = 0
    stack = []
    stack.append((start, 0))

    far_info = (start, 0)

    while stack:
        now_info = stack.pop()
        distance[now_info[0]] = now_info[1]

        if far_info[1] < now_info[1]:
            far_info = now_info
        
        for edge in edges[now_info[0]]:
            if distance[edge[0]] == -1:
                stack.append((edge[0], now_info[1] + edge[1]))

    return far_info

n = int(input())

edges = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, cost = map(int, input().split())
    edges[a].append((b, cost))
    edges[b].append((a, cost))


(far_one, dist_temp) = dfs(1)
(far_other, answer) = dfs(far_one)

# print(far_one, dist_temp)
# print(far_other, answer)

print(answer)
