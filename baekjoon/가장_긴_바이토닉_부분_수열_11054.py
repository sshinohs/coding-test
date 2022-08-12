import sys

input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

dp = [[1]*2 for _ in range(N)]

max_count = 1

for i in range(1, N):
    for j in range(i-1, -1, -1):
        if data[j] < data[i]:
            if dp[i][0] < dp[j][0] + 1:
                dp[i][0] = dp[j][0] + 1
                if max_count < dp[i][0]:
                    max_count = dp[i][0]
        if data[j] > data[i]:
            check = max(dp[j]) + 1
            if dp[i][1] < check:
                dp[i][1] = check
                if max_count < dp[i][1]:
                    max_count = dp[i][1]

print(max_count)