from itertools import combinations
from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

N, S = map(int, input().split())

nums = list(map(int, input().split()))

# N = 40
# S = 10
# nums = [i for i in range(N)]

A = nums[:N//2]
B = nums[N//2:]

count = 0

A_sums = []
for i in range(1, len(A)+1):
    for j in combinations(A, i):
        A_sums.append(sum(j))
        if A_sums[-1] == S:
            count += 1

B_sums = []
for i in range(1, len(B)+1):
    for j in combinations(B, i):
        B_sums.append(sum(j))
        if B_sums[-1] == S:
            count += 1

idx_A = 0
idx_B = 0

len_A_sums = len(A_sums)
len_B_sums = len(B_sums)

A_sums.sort()
B_sums.sort()

for A_elem in A_sums:
    check = S - A_elem
    count += bisect_right(B_sums, check) - bisect_left(B_sums, check)

# print('why')
# print(bisect_right(B_sums, 3))

# print(A_sums)
# print(B_sums)


print(count)
