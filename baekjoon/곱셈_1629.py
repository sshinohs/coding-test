import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

def devide_conquer(a, b):
    if b == 1:
        return a % C
    
    temp = devide_conquer(a, b//2)

    if b % 2 == 0:
        return temp **2 % C
    else:
        return temp **2 * a % C

print(devide_conquer(A, B))