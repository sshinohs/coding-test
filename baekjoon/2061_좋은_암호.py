import sys

input = sys.stdin.readline

K, L = map(int, input().split())

flag = True

for i in range(2, L):
    if K % i == 0:
        check = i
        flag = False
        break


if flag:
    print('GOOD')
else:
    print('BAD', check)