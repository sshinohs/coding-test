import sys

input = sys.stdin.readline

data = list(map(int, input().split()))
data.sort()

# print(data)

nums = data[:]

count = 1
while True:
    # print(nums[count%2], nums[(count+1)%2])
    remainder = nums[count%2] % nums[(count+1)%2]
    if remainder % nums[count%2] == 0:
        break
    nums[count%2] = remainder
    count += 1

GCD = nums[(count+1)%2]

LCM = data[0]*data[1]//GCD

print(GCD)
print(LCM)

