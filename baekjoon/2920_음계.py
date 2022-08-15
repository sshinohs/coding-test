import sys

input = sys.stdin.readline

flag_ascend = True
flag_descend = True
for i, val in enumerate(map(int, input().split())):
    if i+1 != val:
        flag_ascend = False
    if 8-i != val:
        flag_descend = False

if flag_ascend:
    print('ascending')
elif flag_descend:
    print('descending')
else:
    print('mixed')