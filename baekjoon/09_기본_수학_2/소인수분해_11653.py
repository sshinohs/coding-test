import sys

input = sys.stdin.readline

N = int(input())

remain = N

now = 2
while remain > 1:
    if remain % now == 0:
        print(now)
        remain //= now
    else:
        now += 1