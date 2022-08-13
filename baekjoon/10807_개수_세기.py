import sys

input = sys.stdin.readline

N = int(input())

count = 0

nums = list(map(int, input().split()))

V = int(input())

for i in range(N):
    if nums[i] == V:
        count += 1

print(count)