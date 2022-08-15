import sys

input = sys.stdin.readline

S, M = map(int, input().split())

if S < 1024:
    output = 'No thanks'
else:
    remain = S - 1023
    flag = True
    for i in range(11):
        checker = 1 << i
        if (remain & checker) != 0 and (M & checker) == 0:
            flag = False
    if flag:
        output = 'Thanks'
    else:
        output = 'Impossible'

print(output)