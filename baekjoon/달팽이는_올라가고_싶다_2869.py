import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

one_day_step = B-A

output = (B - V) // one_day_step

if (B - V) % one_day_step != 0:
    output += 1

print(output)