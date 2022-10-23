import sys

input = sys.stdin.readline

people = list(map(int, input().split()))

x, y, r = map(int, input().split())

for i, human in enumerate(people):
    if human == x:
        print(i+1)
        break
else:
    print(0)

