import sys

input = sys.stdin.readline


while True:
    try:
        a, b, c = map(int, input().split())
    except:
        break

    ab = b - a
    bc = c - b
    if ab >= bc:
        print(ab-1)
    else:
        print(bc-1)