## by 3juhwan
import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[0]*2 for __ in range(n+1)]
    
    for i in range(n):
        print('%%')
        print(i)
        print(dp)
        
        x = a[i]
        dp[x][i&1] = max(dp[x][i&1], dp[x][not(i&1)]+1)
        print(dp)
    for i in range(1, n+1):
        print(max(dp[i]), end=' ')
    print()

    
    
    
 
for __ in range(int(input())):
    solve()
    # print('YES' if solve() else 'NO')


# import sys

# input = sys.stdin.readline

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     board = [[0]*3 for _ in range(n+1)]

#     for i, num in enumerate(map(int, input().split())):
#         if board[num][0] == 0 or (i - board[num][2])%2 == 1:
#             board[num][2] = i
#             board[num][1] += 1
#             if board[num][0] < board[num][1]:
#                 board[num][0] = board[num][1]
#         else:
#             board[num][2] = i
#             board[num][1] = 1
    
#     for boa in board[1:]:
#         print(boa[0], end=' ')
#     print()