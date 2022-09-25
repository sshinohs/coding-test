import sys

input = sys.stdin.readline

data = []
for _ in range(5):
    data.append(int(input()))

print(min(data[:3]) + min(data[3:]) - 50)