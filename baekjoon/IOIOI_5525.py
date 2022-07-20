import sys

input = sys.stdin.readline

N = int(input())

M = int(input())

S = input().strip()

count = 0
cumul = 0
now_idx = 0
while now_idx < M:
    if S[now_idx] == 'I':
        while S[now_idx+1:now_idx+3] == 'OI':
            now_idx += 2
            cumul += 1
            if cumul >= N:
                count += 1
        cumul = 0
        now_idx += 1
    else:
        now_idx += 1

print(count)