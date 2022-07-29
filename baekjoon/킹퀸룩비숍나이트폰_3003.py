import sys

input = sys.stdin.readline

data = list(map(int, input().split()))

criteria = [1, 1, 2, 2, 2, 8]

for i in range(len(criteria)):
    print(criteria[i] - data[i], end=' ')