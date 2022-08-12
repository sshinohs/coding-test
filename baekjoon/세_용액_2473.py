import sys
import math

input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

data.sort()

best_set = []
best = math.inf

for i in range(N):

    pre_num = data[i]
    candidates = data[:i] + data[i+1:]

    st = 0
    ed = N-2

    while st < ed:
        
        check = candidates[st] + candidates[ed] + pre_num
        
        if best > abs(check):
            best = abs(check)
            best_set = [pre_num, candidates[st], candidates[ed]]
        
        if check == 0:
            break
        if check > 0:
            ed -= 1
        if check < 0:
            st += 1

best_set.sort()
for num in best_set:
    print(num, end=' ')