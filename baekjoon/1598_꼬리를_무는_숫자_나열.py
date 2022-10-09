import sys

input = sys.stdin.readline

a, b = map(int, input().split())

a -= 1
b -= 1

ap = (a // 4, a % 4)
bp = (b // 4, b % 4)

print(abs(ap[0] - bp[0]) + abs(ap[1] - bp[1]))