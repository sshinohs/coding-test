import sys
# import math

input = sys.stdin.readline

N = int(input())

meetings = []
MAX = 0
for _ in range(N):
    val = tuple(map(int, input().split()))
    meetings.append(val)
    if MAX < val[1]:
        MAX = val[1]

meetings.sort(key = lambda x : (x[1], x[0]))

max_arr = [0] * 1000001
max_val = [0, 0]

for meeting in meetings:
    if meeting[0] >= max_val[1]:
        max_arr[meeting[1]] = max(max_val[0]+1, max_arr[meeting[1]], max_arr[meeting[0]] + 1)
    else:
        max_arr[meeting[1]] = max(max_arr[meeting[1]], max_arr[meeting[0]] + 1)
    if max_arr[meeting[1]] > max_val[0]:
        max_val = [max_arr[meeting[1]], meeting[1]]
    else:
        max_arr[meeting[1]] = max_val[0]
print(max(max_arr))