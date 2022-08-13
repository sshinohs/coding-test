import sys

input = sys.stdin.readline

N = int(input())

count_five = N // 5

while count_five >= 0:
    if (N - count_five * 5) % 3 == 0:
        a = (N - count_five * 5) // 3
        answer = count_five + a
        break
    count_five -= 1
else:
    if N % 3 == 0:
        answer = N // 3
    else:
        answer = -1

print(answer)