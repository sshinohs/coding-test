import sys
input = sys.stdin.readline

N = int(input())

count = 0

nums = [0, 0, 1, 1]

for i in range(4, N+1):
    temp = []
    if i%2 == 0:
        temp.append(nums[i//2])
    if i%3 == 0:
        temp.append(nums[i//3])
    temp.append(nums[i-1])
    nums.append(min(temp)+1)

print(nums[N])