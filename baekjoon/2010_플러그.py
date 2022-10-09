import sys

input = sys.stdin.readline

init = 1
for _ in range(int(input())):
    init += int(input())
    init -= 1

print(init)