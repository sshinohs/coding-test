import sys

input = sys.stdin.readline

data = input()[:-1]

if data == data[::-1]:
    print(1)
else:
    print(-1)