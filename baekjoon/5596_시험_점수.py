import sys
input = sys.stdin.readline

S = sum(map(int, input().split()))
T = sum(map(int, input().split()))

print(max(S, T))