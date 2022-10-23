import sys

input = sys.stdin.readline

A, B, C, D = map(int, input().split())

print(abs((C + B) - (D + A)))