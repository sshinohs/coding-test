import sys

input = sys.stdin.readline

now = 1
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == now:
        now = b
    elif b == now:
        now = a

print(now)