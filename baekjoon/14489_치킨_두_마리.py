import sys

input = sys.stdin.readline

A, B = map(int, input().split())

chik = int(input())



total = A + B

if total >= 2*chik:
    print(total - 2*chik)
else:
    print(total)