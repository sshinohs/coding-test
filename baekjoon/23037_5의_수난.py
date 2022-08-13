import sys

input = sys.stdin.readline

n = input()[:-1]

sum = 0
for i in n:
    sum += int(i) ** 5

print(sum)

