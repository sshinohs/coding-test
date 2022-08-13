import sys

input = sys.stdin.readline

N = int(input())

steps = []

cumul = [[0, 0] for _ in range(N+2)]

for _ in range(N):
    steps.append(int(input()))


for i in range(2, N+2):
    cumul[i][0] = cumul[i-1][1] + steps[i-2]
    cumul[i][1] = max(cumul[i-2]) + steps[i-2]

# print(steps)

print(cumul)

print(max(cumul[-1]))

# print(cumul)