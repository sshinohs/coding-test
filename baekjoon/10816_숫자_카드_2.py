import sys
input = sys.stdin.readline

N = int(input())

cards_dict = {}

for i in map(int, input().split()):
    if i not in cards_dict:
        cards_dict[i] = 1
    else:
        cards_dict[i] += 1

M = int(input())

for i in map(int, input().split()):
    if i in cards_dict:
        print(cards_dict[i])
    else:
        print(0)

