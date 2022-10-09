import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

check = a*b - c

if check < 0:
    print(0)
else:
    print(check)