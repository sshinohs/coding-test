import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    max_value = max(data)
    max_idx = data.index(max_value)
    diff = []

    flag = True
    for i in range(max_idx):
        if data[i+1] - data[i] < 0:
            flag = False
    
    for i in range(max_idx, n-1):
        if data[i+1] - data[i] > 0:
            flag = False
    
    if flag:
        print('YES')
    else:
        print('NO')