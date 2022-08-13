import sys

input = sys.stdin.readline

dp = [1, 1]

n = int(input())

for _ in range(2, n+1):
    dp.append((dp[-2]*2 + dp[-1])%10007)

print(dp[n])