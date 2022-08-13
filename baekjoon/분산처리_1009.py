import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    loop = [a**1 % 10]
    count = 2
    while (a ** count) % 10 != loop[0]:
        loop.append((a ** count) % 10)
        count += 1
    
    check = loop[b % len(loop) - 1]
    if check == 0:
        print(10)
    else:
        print(check)