import sys
input = sys.stdin.readline

N = int(input())

words = {}
for _ in range(N):
    word = input()
    word = word[:-1]
    if word not in words:
        words[word] = len(word)
# print(words)
answer = sorted(words.items(), key = lambda item : (item[1], item[0]))

for ans in answer:
    print(ans[0])