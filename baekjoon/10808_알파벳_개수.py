import sys

input = sys.stdin.readline

data = input().strip()

output = [0] * 26
for cha in data:
    output[ord(cha)-ord('a')] += 1

for i in output:
    print(i, end=' ')
print()