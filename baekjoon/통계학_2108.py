import sys
import math

input = sys.stdin.readline

N = int(input())

nums = []

nums_dict = {}

for _ in range(N):
    num = int(input())
    nums.append(num)
    if num not in nums_dict:
        nums_dict[num] = 1
    else:
        nums_dict[num] += 1


nums.sort()
nums_avg = round(sum(nums)/N)
nums_center = nums[N//2]

print(nums_avg)
print(nums_center)
mode_arr = sorted(nums_dict.items(), key = lambda x: x[1], reverse=True)

modes = []

count = 0
while count < len(mode_arr):
    if mode_arr[count][1] == mode_arr[0][1]:
        modes.append(mode_arr[count][0])
        count += 1
    else:
        break

modes.sort()

if len(modes) < 2:
    print(modes[0])
else:
    print(modes[1])

print(nums[-1] - nums[0])
