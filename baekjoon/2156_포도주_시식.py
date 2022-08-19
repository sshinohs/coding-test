import sys

input = sys.stdin.readline

n = int(input())

drink = []
for _ in range(n):
    drink.append(int(input()))

dp = [(0, 0, 0), (0, 0, 0)]
# 0개연속 최고, 1개연속 최고, 2개연속 최고

max_val = 0
for num in drink:
    a = max(dp[-1])
    b = dp[-1][0] + num
    c = dp[-1][1] + num
    dp.append((a, b, c))

print(dp)
print(max(dp[-1]))