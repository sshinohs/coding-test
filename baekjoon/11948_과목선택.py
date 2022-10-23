import sys
input = sys.stdin.readline


dataA = []
for _ in range(4):
    dataA.append(int(input()))

dataB = []
for _ in range(2):
    dataB.append(int(input()))


print(sum(dataA) + sum(dataB) - min(dataA) - min(dataB))