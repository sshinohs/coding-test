import sys
import math

input = sys.stdin.readline

N, C = map(int, input().split())

data = []

for _ in range(N):
    data.append(int(input()))

data.sort()
max_val = data[-1]
min_val = data[0]

st = 1
ed = (max_val - min_val) // (C - 1)


def router_num(data, dist):
    count = 0
    before = -math.inf
    for pos in data:
        if pos - before >= dist:
            count += 1
            before = pos
    return count

def binary_search(data, st, ed, target):

    left = st
    right = ed

    while left <= right:
        mid = (left + right) // 2
        check = router_num(data, mid)
        if check < target:
            right = mid - 1
        else:
            tmp = mid
            left = mid + 1
    
    return tmp

print(binary_search(data, st, ed, C))