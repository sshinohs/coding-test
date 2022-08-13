import sys

input = sys.stdin.readline

N = int(input())

default_dist = abs(N-100)
max_dist = default_dist

set_num = 100

# search_range = (N-max_dist, N+max_dist)
flag = False

M = int(input())

broken = {}

# if M != 0:
for i in map(int, input().split()):
    broken[i] = 1

# print(broken)

# print('%%')
for i in range(N, max(0, N-max_dist+1)-1, -1):
    # print(i)
    # print('hong')
    for cha in str(i):
        # print('cha', cha)
        if int(cha) in broken:
            # print('zza')
            break
    else:
        if max_dist>N-i:
            # print('ho')
            # print(max_dist)
            max_dist = N-i
            set_num = i
            flag = True
            break
# print('%%')

for i in range(N, N+max_dist):
    # print('hong')
    for cha in str(i):
        # print('cha', cha)
        if int(cha) in broken:
            # print('zza')
            break
    else:
        if max_dist>i-N:
            # print('ho')
            # print(max_dist)
            max_dist = i-N
            set_num = i
            flag = True
            break

if flag:
    output = min(len(str(set_num)) + max_dist, default_dist)
else:
    output = default_dist

# print('%%')
# print(max_dist)
# print(set_num)

print(output)
