import sys
input = sys.stdin.readline

N = int(input())

nums = []
for _ in range(N):
    nums.append(list(map(int, input().split())))

answer = sorted(nums, key = lambda x: (x[0], x[1]))

for an in answer:
    print(*an)