import sys
input = sys.stdin.readline

S = input().strip()

len_S = len(S)

cha_set = set()
for i in range(len_S):
    for j in range(len_S-i):
        cha_set.add(S[j:j+i+1])

print(len(cha_set))