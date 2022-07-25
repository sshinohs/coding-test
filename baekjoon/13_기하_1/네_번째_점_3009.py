import sys

input = sys.stdin.readline

x_box = []
y_box = []

for _ in range(3):
    a, b = map(int, input().split())
    if a in x_box:
        x_box.remove(a)
    else:
        x_box.append(a)
    if b in y_box:
        y_box.remove(b)
    else:
        y_box.append(b)

print(x_box[0], y_box[0])