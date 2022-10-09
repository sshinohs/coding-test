import sys

input = sys.stdin.readline


while True:
    data = input().strip()
    if data == '0':
        break

    count = len(data) + 1

    for num in data:
        num = int(num)
        if num == 1:
            count += 2
        elif num == 0:
            count += 4
        else:
            count += 3

    print(count)