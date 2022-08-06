import sys
import math

input = sys.stdin.readline

def find_permutation(arr, n):
    if arr[n] != math.inf:
        return arr[n]
    else:
        check = math.floor(math.sqrt((n-1)*2))
        return find_permutation(arr, check**2-(n-1)) + list(range((n-1), check**2-(n-1)-1, -1))

dp = [math.inf for _ in range(10**5 + 1)]
dp[0] = []
dp[1] = [0]
dp[2] = [1, 0]

for _ in range(int(input())):
    n = int(input())
    answer = find_permutation(dp, n)
    for num in answer:
        print(num, end=' ')
    print()