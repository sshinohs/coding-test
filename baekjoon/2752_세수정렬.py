import sys

input = sys.stdin.readline

data = list(map(int,input().split()))

data.sort()

for i in data:
    print(i, end=' ')
print()