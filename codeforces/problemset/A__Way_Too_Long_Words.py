import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    word = input().rstrip()
    len_word = len(word)
    if len_word < 10:
        print(word)
    else:
        print(word[0]+ str(len_word-2) + word[-1])

