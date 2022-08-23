import sys

input = sys.stdin.readline

N, K = map(int, input().split())

count = 0
num = 1
while num <= N:
    if N % num == 0:
        count += 1
        if count == K:
            print(num)
            break
    num += 1
else:
    print(0)