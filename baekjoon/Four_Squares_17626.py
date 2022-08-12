import sys
import math

input = sys.stdin.readline

dp = [math.inf] * (50001)

dp[0] = 0

count = 1
while count ** 2 <= 50000:
    dp[count ** 2] = 1
    count += 1

def fs(dp, num):
    best = math.inf
    max_sqrt = math.floor(math.sqrt(num))
    for i in range(max_sqrt, 0, -1):
        a = i**2
        b = num - i**2
        if dp[a] == math.inf:
            dp[a] = fs(dp, a)
        if dp[b] == math.inf:
            dp[b] = fs(dp, b)
        
        if best > dp[a] + dp[b]:
            best = dp[a] + dp[b]
    return best

print(fs(dp, int(input())))