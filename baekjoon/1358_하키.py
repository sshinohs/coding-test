import sys

input = sys.stdin.readline

W, H, X, Y, P = map(int, input().split())

R = H/2

count = 0
for _ in range(P):
    x, y = map(int, input().split())
    a = x >= X and x <= X+W and y >= Y and y <= Y+H
    b = ((X - x)**2 + (Y + H/2 - y)**2) <= R**2
    c = ((X + W - x)**2 + (Y + H/2 - y)**2) <= R**2
    if a or b or c:
        count += 1

print(count)