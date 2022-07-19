from re import A
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    data = ['B']*m
    operations = map(int, input().split())
    
    for oper in operations:
        oper_inv = m + 1 - oper
        if oper <= oper_inv:
            a = oper
            b = oper_inv
        else:
            a = oper_inv
            b = oper
        if data[a-1] == 'B':
            data[a-1] = 'A'
        else:
            data[b-1] ='A'
    
    print(''.join(data))

    