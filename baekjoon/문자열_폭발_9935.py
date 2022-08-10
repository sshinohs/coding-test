import sys
from collections import deque

input = sys.stdin.readline

print = sys.stdout.write

data = input().strip()

bomb = input().strip()

len_bomb = len(bomb)

flag = True
if len_bomb == 1:
    for cha in data:
        if cha != bomb[0]:
            flag = False
            print(cha)
    if flag:
        print('FRULA\n')
    else:
        print('\n')
else:
    dq = deque()
    nxt = 0
    for cha in data:
        if cha == bomb[0]:
            dq.append(0)
            nxt = 1
        elif cha == bomb[nxt]:
            if nxt + 1 == len_bomb:
                for _ in range(len_bomb-1):
                    dq.pop()
                if dq:
                    nxt = dq[-1] + 1
                else:
                    nxt = 0
            else:
                dq.append(nxt)
                nxt += 1
        else:
            flag = False
            while dq:
                print(bomb[dq.popleft()])
            print(cha)
            nxt = 0

    while dq:
        flag = False
        print(bomb[dq.popleft()])

    if flag:
        print('FRULA\n')
    else:
        print('\n')