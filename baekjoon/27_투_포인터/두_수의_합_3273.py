import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

nums.sort()

x = int(input())


left = 0
right = n-1

count = 0
while left != right:
    val = nums[left] + nums[right]
    if x == val:
        count += 1
        # right -= 1
        left += 1
    elif x < val:
        right -= 1
    elif x > val:
        left += 1

print(count)
