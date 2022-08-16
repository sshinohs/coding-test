import sys

input = sys.stdin.readline

receipt = int(input())

total = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    total += a*b

if receipt == total:
    print('Yes')
else:
    print('No')