import sys

input = sys.stdin.readline

L, P = map(int, input().split())

total = L*P

for i in map(int, input().split()):
    print(i - total, end=' ')
print()
