import sys

input = sys.stdin.readline

K = int(input())

pos = [(0, 0)]

circular = [0, 4, 3, 1, 2]
horizon_max = 0
vertical_max = 0

data = []
x_max = 0
y_max = 0
for _ in range(6):
    a, b = map(int, input().split())
    data.append((a, b))
    if a == 1 or a == 2:
        if b > y_max:
            y_max = b
    else:
        if b > x_max:
            x_max = b


for i in range(5):
    if data[i+1][0] != circular[data[i][0]]:
        concave = data[i][1]*data[i+1][1]
        break
else:
    concave = data[0][1]*data[5][1]

shell = x_max * y_max

print((shell - concave) * K)