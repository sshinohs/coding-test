import sys

loop_num = int(sys.stdin.readline().rstrip())

for ii in range(loop_num):
    data = sys.stdin.readline().rstrip()
    nums = data.split()
    a = int(nums[0])
    b = int(nums[1])
    print(a+b)