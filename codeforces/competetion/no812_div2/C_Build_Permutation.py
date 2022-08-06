import sys
import math

input = sys.stdin.readline

dp = [[], [0], [1, 0]]

for _ in range(int(input())):
    n = int(input())
    if n + 1 <= len(dp):
        for num in dp[n]:
            print(num, end=' ')
        print()
    else:
        for i in range(len(dp), n+1):
            check = math.floor(math.sqrt((i-1)*2))
            dp.append(dp[check**2-(i-1)] + list(range((i-1), check**2-(i-1)-1, -1)))
        for num in dp[n]:
            print(num, end=' ')
        print()


