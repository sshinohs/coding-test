import sys

input = sys.stdin.readline

cumulation = 0
for val in map(int, input().split()):
    cumulation += val**2

print(cumulation%10)