import sys

input = sys.stdin.readline


N = int(input())

data = list(map(int, input().split()))

data.sort()

# print(data)
cumul = 0
answer = 0
for num in data:
    answer += num + cumul
    cumul += num

print(answer)