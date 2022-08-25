import sys

input = sys.stdin.readline

while True:
    count = 0
    data = input().strip()
    if data == '#':
        break
    for cha in data:
        if cha == 'a' or cha == 'e' or cha == 'i' or cha == 'o' or cha == 'u' or cha == 'A' or cha == 'E' or cha == 'I' or cha == 'O' or cha == 'U':
            count += 1
    print(count)
    