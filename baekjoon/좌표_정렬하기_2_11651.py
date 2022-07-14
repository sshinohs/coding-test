import sys

input = sys.stdin.readline


N = int(input())

arr = []

for _ in range(N):
    arr.append(tuple(map(int, input().split())))

# print(arr)

arr.sort(key = lambda x: (x[1], x[0]))

for row in arr:
    for num in row:
        print(num, end= ' ')
    print()