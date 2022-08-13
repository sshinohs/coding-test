import sys

input = sys.stdin.readline


N, M = map(int, input().split())

name_to_num = {}

num_to_name = {}

for i in range(N):
    name = input()
    name_to_num[name[:-1]] = i+1
    num_to_name[i+1] = name[:-1]

for i in range(M):
    command = input()
    if command[:-1].isdigit():
        print(num_to_name[int(command[:-1])])
    else:
        print(name_to_num[command[:-1]])