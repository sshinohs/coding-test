import sys

input = sys.stdin.readline

def dfs(start):
    far = (start, 0)
    distance = [-1] * (V + 1)
    stack = []
    stack.append((start, 0))
    while stack:
        # print('$$')
        # print(stack)
        now = stack.pop()
        distance[now[0]] = now[1]
        if far[1] < now[1]:
            far = now
        for edge in edges_arr[now[0]]:
            if distance[edge[0]] == -1:
                stack.append((edge[0], distance[now[0]] + edge[1]))
    # print(distance)
    return far

V = int(input())

edges_arr = [[] for _ in range(V+1)]
for _ in range(V):
    node_data = input().split()
    node_num = int(node_data[0])
    edges = []
    for i in range(1,len(node_data)-1, 2):
        edges.append((int(node_data[i]), int(node_data[i+1])))
    edges_arr[node_num] = edges

# print(edges_arr)

[far_one, dist] = dfs(1)
[far_other, answer]= dfs(far_one)

# print(far_one, dist)
# print(far_other, answer)

print(answer)
    