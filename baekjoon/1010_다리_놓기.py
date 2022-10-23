import sys

input = sys.stdin.readline

import sys

input = sys.stdin.readline


for _ in range(int(input())):
    N, M = map(int, input().split())
    base = N
    df = M-N
    
    count = 1
    for i in range(1, df+1):
        count += 1 + (base-1) * (i-1)
    
    print(count)