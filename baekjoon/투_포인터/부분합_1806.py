import sys

input = sys.stdin.readline

N, S = map(int, input().split())
# N = 10
# S = 21

nums = list(map(int, input().split()))
# nums = list(map(int, '5 1 3 5 10 7 4 9 2 8'.split()))
# nums = list(map(int, '11 2 5 6 8 9 2 3 10 9 10'.split()))

# nums.sort()

sums = [0]

for i in nums:
    sums.append(sums[-1]+i)


# print(nums)
# print(sums)

left = 0
right = 1

INF = 1000000001

min_len = INF

while left <= right and right <= len(nums):
    # val = sum(nums[left:right])
    val = sums[right]-sums[left]
    # print(val)
    if S > val:
        right += 1
    elif S == val:
        if min_len > right-left:
            min_len = right-left
        right += 1
    elif S < val:
        if min_len > right-left:
            min_len = right-left
        left += 1

if min_len == INF:
    print(0)
else:    
    print(min_len)