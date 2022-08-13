from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()

for series in permutations(nums, M):
    for i in series:
        print(i, end=' ')
    print()