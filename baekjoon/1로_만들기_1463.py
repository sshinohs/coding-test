import sys
input = sys.stdin.readline

N = int(input())

count = 0

nums = [0, 0, 1, 1]

for i in range(4, N+1):
    temp = []
    if i%2 == 0:
        temp.append(nums[i//2])
    if i%3 == 0:
        temp.append(nums[i//3])
    temp.append(nums[i-1])
    nums.append(min(temp)+1)

print(nums[N])



##### BFS를 이용한 풀이 ########### (더 느리다)
# import sys
# import math
# from collections import deque

# input = sys.stdin.readline

# N = int(input())

# count_arr = [math.inf] * (N+1)

# count_arr[0] = 0
# count_arr[1] = 0

# q = deque()

# q.append(1)

# while q:
#     now = q.popleft()
#     if now == N:
#         print(count_arr[N])
#         break
#     else:
#         nxt_candi = [now+1, now*2, now*3]
#         for nxt in nxt_candi:
#             if nxt <= N and count_arr[nxt] == math.inf:
#                 count_arr[nxt] = count_arr[now] + 1
#                 q.append(nxt)

# print(count_arr)