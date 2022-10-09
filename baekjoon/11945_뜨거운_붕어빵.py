import sys

input = sys.stdin.readline


N, M = map(int, input().split())

for _ in range(N):
    print(''.join(list(input().strip())[::-1]))
    