import sys
# import math
from collections import deque
input = sys.stdin.readline

n = int(input())

# memo = [math.inf] * (n+2)
memo = {}
memo[0] = 0
memo[1] = 1

def fibo(n):
    if n in memo:
        return memo[n]
    else:
        if n % 2 == 0:
            memo[n//2] = fibo(n//2) % 1000000007
            memo[n//2-1] = fibo(n//2-1) % 1000000007
            memo[n] = (fibo(n//2) * (fibo(n//2) + 2 * fibo(n//2-1))) % 1000000007
            # return memo[n//2] * (memo[n//2] + 2 * memo[n//2-1]) % 1000000007
            return memo[n]
        else:
            memo[n//2+1] = fibo(n//2+1) % 1000000007
            memo[n//2] = fibo(n//2) % 1000000007
            memo[n] = (fibo(n//2+1) ** 2 + fibo(n//2) ** 2) % 1000000007
            # return memo[n//2+1] ** 2 + memo[n//2] ** 2 % 1000000007
            return memo[n]
print(fibo(n))

# dp = dict()

# def fibo2(n):
#       if dp.get(n) != None:
#             return dp[n]
#       if n == 0:
#             return 0
#       if n == 1 or n == 2:
#             return 1
#       if n % 2 == 0:
#             dp[n // 2 + 1] = fibo2(n // 2 + 1) % 1000000007 # 맨 처음에는 % 1000000007을 해주지 않아 시간초과가 났었다..
#             dp[n // 2 - 1] = fibo2(n // 2 - 1) % 1000000007
#             return dp[n // 2 + 1] ** 2 - dp[n // 2 - 1] ** 2
#       else:
#             dp[n // 2 + 1] = fibo2(n // 2 + 1) % 1000000007
#             dp[n // 2] = fibo2(n // 2) % 1000000007
#             return dp[n // 2 + 1] ** 2 + dp[n // 2] ** 2

# # print(fibo(int(input())) % 1000000007)

# for i in range(45, 46):
#     # check = fibo(i) - fibo2(i)%1000000007
#     # if check != 0:
#     #     print(i)
#     print(fibo(i)%1000000007, fibo2(i)%1000000007)