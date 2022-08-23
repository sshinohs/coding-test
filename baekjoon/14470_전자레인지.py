import sys

input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())


count = 0

if A <= 0:
    count += abs(A) * C + D
    count += B * E
else:
    count += (B-A) * E

print(count)