import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    q = deque()
    priority_arr = []
    N, M = map(int, input().split())
    for i, priority in enumerate(map(int, input().split())):
        q.append((priority, i))
        priority_arr.append(priority)
    
    priority_arr.sort()
    
    count = 0
    while True:
        if q[0][0] < priority_arr[-1]:
            temp = q.popleft()
            q.append(temp)
        else:
            count += 1
            priority_arr.pop()
            if q.popleft()[1] == M:
                print(count)
                break