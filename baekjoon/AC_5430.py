import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().strip()
    n = int(input())
    nums = input().strip()
    if n == 0:
        nums = deque()
    else:
        nums = deque(map(int, nums[1:-1].split(',')))

    inv = False
    
    for oper in p:
        if oper == 'R':
            inv = not inv
        if oper == 'D':
            if n == 0:
                print('error')
                break
            else:
                if inv:
                    nums.pop()
                    n -= 1
                else:
                    nums.popleft()
                    n -= 1
    else:
        # print(nums)
        if inv:
            output = '['
            for i in range(len(nums)-1, -1, -1):
                output += str(nums[i])
                output += ','
            if len(output)>1:
                output = output[:-1] + ']'
            else:
                output += ']'
            print(output)
        else:
            output = '['
            for i in range(len(nums)):
                output += str(nums[i])
                output += ','
            if len(output)>1:
                output = output[:-1] + ']'
            else:
                output += ']'
            print(output)
