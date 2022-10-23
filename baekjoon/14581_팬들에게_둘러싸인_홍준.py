import sys

input = sys.stdin.readline
fan = ':fan:'

data = input().strip()

name = ':' + data + ':'

for _ in range(3):
    print(fan, end='')
print()

print(fan, end='')
print(name, end='')
print(fan, end='')
print()

for _ in range(3):
    print(fan, end='')
print()