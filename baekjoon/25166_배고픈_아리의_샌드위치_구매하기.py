import sys

input = sys.stdin.readline

S, M = map(int, input().split())

print(bin(M)[2:][::-1])