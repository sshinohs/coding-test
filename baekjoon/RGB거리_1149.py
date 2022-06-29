import sys

input = sys.stdin.readline

N = int(input())

min_arr = [0, 0, 0]

for _ in range(N):
    costs = list(map(int, input().split()))
    a = min(min_arr[1], min_arr[2]) + costs[0]
    b = min(min_arr[2], min_arr[0]) + costs[1]
    c = min(min_arr[0], min_arr[1]) + costs[2]
    min_arr = [a, b, c]

print(min(min_arr))