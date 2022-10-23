import sys

input = sys.stdin.readline

N = int(input())

score = 0
cumul = 1

for check in map(int, input().split()):
    if check == 1:
        score += cumul
        cumul += 1
    else:
        cumul = 1

print(score)