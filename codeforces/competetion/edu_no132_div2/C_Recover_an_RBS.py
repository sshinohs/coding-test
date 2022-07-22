import sys
from collections import deque

def dfs(data):
    available = 0
    len_data = len(data)
    idx = 0
    count = 0

    while True:
        if idx == len_data:
            if count == 0:
                return 'YES'
            else:
                return 'NO'
        if data[idx] == '(':
            count += 1
            idx += 1
            continue
        elif data[idx] == ')':
            count -= 1
            idx += 1
            continue
        if count < 0:
            return 'NO'
        if data[idx] == '?':
            break

    stack = deque()
    stack.append([idx+1, count+1])
    stack.append([idx+1, count-1])
    while stack:
        now = stack.pop()
        print(now)
        question = False
        while True:
            if now[0] == len_data:
                if now[1] == 0:
                    if available == 1:
                        return 'NO'
                    else:
                        available += 1
                        break
                else:
                    break
            if data[now[0]] == '(':
                now[1] += 1
                now[0] += 1
                continue
            elif data[now[0]] == ')':
                now[1] -= 1
                now[0] += 1
                continue
            if now[1] < 0:
                return 'NO'
            if data[now[0]] == '?':
                question = True
                break
        if question:
            stack.append([now[0]+1, now[1]+1])
            stack.append([now[0]+1, now[1]-1])
    return 'YES'

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    data = input().rstrip()
    print(dfs(data))