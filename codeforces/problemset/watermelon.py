import sys

input = sys.stdin.readline

weight = int(input())

if weight % 2 != 0 or weight == 2:
    print('NO')
else:
    print('YES')