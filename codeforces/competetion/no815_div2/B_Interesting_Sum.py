import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()
    print(- data[0] - data[1] + data[-1] + data[-2])