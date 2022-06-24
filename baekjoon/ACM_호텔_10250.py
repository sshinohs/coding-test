import sys

input = sys.stdin.readline

case_num = int(input())

for _ in range(case_num):
    h, w, n = map(int, input().split())

    ho_num = (n-1)//h + 1
    floor_num = n%h
    if floor_num == 0:
        floor_num = h

    if ho_num < 10:
        print(str(floor_num)+str(0)+str(ho_num))
    else:
        print(str(floor_num)+str(ho_num))
