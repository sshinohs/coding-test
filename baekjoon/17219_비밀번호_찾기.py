import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pw_dict = {}

for _ in range(N):
    a, b = input().strip().split()
    pw_dict[a] = b

for _ in range(M):
    print(pw_dict[input().strip()])