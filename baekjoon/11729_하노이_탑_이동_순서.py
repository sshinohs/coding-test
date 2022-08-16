import sys
import math

input = sys.stdin.readline

N = int(input())

record = []
def hannoi(fr, to, num):
    if num == 1:
        record.append([round(math.log2(fr))+1, round(math.log2(to))+1])
    else:
        hannoi(fr, 7 ^ (fr | to), num - 1)
        hannoi(fr, to, 1)
        hannoi(7 ^ (fr | to), to, num - 1)

hannoi(0b001, 0b100, N)

print(len(record))

for rec in record:
    print(rec[0], rec[1])