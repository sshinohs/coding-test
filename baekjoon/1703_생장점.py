import sys

input = sys.stdin.readline

while True:
    data = list(map(int, input().split()))

    cumul = 1
    if data[0] == 0:
        break
    for i in range(1, 2*data[0], 2):
        cumul *= data[i]
        cumul -= data[i+1]
    print(cumul)

    