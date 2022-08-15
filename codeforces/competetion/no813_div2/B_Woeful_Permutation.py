import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        for i in range(n//2):
            print((i+1)*2, end=' ')
            print((i+1)*2-1, end=' ')
        print()
    else:
        print(1, end=' ')
        for i in range(n//2):
            print((i+1)*2+1, end=' ')
            print((i+1)*2, end=' ')
        print()