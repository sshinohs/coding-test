import sys
import math

input = sys.stdin.readline

N = int(input())

solutions = list(map(int, input().split()))

st = 0

ed = N-1

best = math.inf
best_set = []

while st < ed:
    check = solutions[st] + solutions[ed]
    
    if best > abs(check):
        best = abs(check)
        best_set = [solutions[st], solutions[ed]]
    
    if check == 0:
        break
    elif check > 0:
        ed -= 1
    elif check < 0:
        st += 1

print(best_set[0], best_set[1])