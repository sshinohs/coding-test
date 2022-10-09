import sys

input = sys.stdin.readline

a = int(input())

count = 0
for i in map(int, input().split()):
    if i == a:
        count += 1

print(count)