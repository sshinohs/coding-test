import sys
from collections import deque

input = sys.stdin.readline

stack = deque()

while True:
    data = input()[:-1]
    if data == '.':
        break
    
    stack = deque()
    
    flag = True
    for cha in data:
        if cha == '(':
            stack.append(cha)
        elif cha == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        elif cha == '[':
            stack.append(cha)
        elif cha ==']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    flag = False
                    break
            else:
                flag = False
                break
    
    if flag:
        if stack:
            print('no')
        else:
            print('yes')
    else:
        print('no')