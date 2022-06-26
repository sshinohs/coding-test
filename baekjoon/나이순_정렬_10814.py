import sys

# 파이썬 sorted 는 안정 정렬임

input = sys.stdin.readline

N = int(input())

members = []

for _ in range(N):
    members.append(input().split())

members.sort(key = lambda x : int(x[0]))

for member in members:
    print(member[0], end=' ')
    print(member[1])