import sys
input = sys.stdin.readline

N = int(input())

data = set()
source = []
for i in map(int, input().split()):
    source.append(i)
    data.add(i)

data = sorted(data)

data_dict = {}
for i, num in enumerate(data):
    data_dict[num] = i

# print(data)


for i in source:
    print(data_dict[i], end=' ')