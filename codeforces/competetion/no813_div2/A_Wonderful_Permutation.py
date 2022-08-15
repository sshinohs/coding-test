import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))

    count = 0

    for num in data[:k]:
        if num > k:
            count += 1
    
    print(count)