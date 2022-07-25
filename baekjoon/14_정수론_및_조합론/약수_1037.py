import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

max_value = nums[0]
min_value = nums[0]
for i in nums:
    if max_value < i:
        max_value = i
    if min_value > i:
        min_value = i

print(max_value * min_value)
    