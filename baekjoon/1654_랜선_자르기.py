import sys
input = sys.stdin.readline

K, N = map(int, input().split())

nums = []

for _ in range(K):
    nums.append(int(input()))


nums.sort()

st = 1
ed = nums[-1]

def line_num(cut_len):
    count_sum = 0
    for num in nums:
        count_sum += num // cut_len
    return count_sum

def binary_search(st, ed):
    while True:
        # print(st, ed)
        target = (st+ed)//2
        output = line_num(target)
        if  output >= N and line_num(target+1) < N:
            return target
        elif output >= N:
            st = target + 1
        elif output < N:
            ed = target - 1
    
print(binary_search(st, ed))
# print(st, ed)
# print(line_num(2))