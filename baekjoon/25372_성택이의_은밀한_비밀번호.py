import sys

input = sys.stdin.readline

for _ in range(int(input())):
    check = len(input().strip())
    if 6 <= check and 9 >= check:
        print('yes')
    else:
        print('no')