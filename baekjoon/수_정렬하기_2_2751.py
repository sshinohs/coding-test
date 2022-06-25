import sys
input = sys.stdin.readline

N = int(input())

nums = [0 for _ in range(2000001)]
for _ in range(N):
    nums[int(input())+1000000] = 1

for i in range(2000001):
    if nums[i] == 1:
        print(i-1000000)