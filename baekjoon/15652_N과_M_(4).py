import sys

input = sys.stdin.readline

N, M = map(int, input().split())

def non_descend(st, ed, m, data):
    if m == 0:
        for num in data:
            print(num, end=' ')
        print()
    else:
        for i in range(st, ed+1):
            data.append(i)
            non_descend(i, ed, m-1, data)
            data.pop()


non_descend(1, N, M, [])