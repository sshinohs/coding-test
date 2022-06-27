import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline


def dfs(arr, i, j):
    arr[i][j] = 0
    if i > 0:
        if arr[i-1][j] == 1:
            dfs(arr, i-1, j)
    if i < len(arr)-1:
        if arr[i+1][j] == 1:
            dfs(arr, i+1, j)
    if j > 0:
        if arr[i][j-1] == 1:
            dfs(arr, i, j-1)
    if j < len(arr[0])-1:
        if arr[i][j+1] == 1:
            dfs(arr, i, j+1)


T = int(input())

answers = []

for _ in range(T):
    M, N, K = map(int, input().split())

    farm = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1

    count = 0

    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                count += 1
                dfs(farm, i, j)

    answers.append(count)

for answer in answers:
    print(answer)