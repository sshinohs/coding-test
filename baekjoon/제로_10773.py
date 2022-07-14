import sys
from collections import deque

input = sys.stdin.readline

K = int(input())

stack = deque()

for _ in range(K):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))