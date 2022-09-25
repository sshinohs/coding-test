import sys

input = sys.stdin.readline

num = int(input())

for _ in range(num//4):
    print('long', end=' ')

print('int')