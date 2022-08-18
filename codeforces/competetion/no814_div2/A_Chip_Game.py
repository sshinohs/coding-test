import sys

input = sys.stdin.readline

for _ in range(int(input())):
    if sum(map(int, input().split()))%2 == 0:
        print('Tonya')
    else:
        print('Burenka')