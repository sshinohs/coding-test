import sys
import heapq

input = sys.stdin.readline

word = input().strip()

len_word = len(word)

hq = []

for i in range(1, len_word-1):
    for j in range(i+1, len_word):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        heapq.heappush(hq, a[::-1] + b[::-1] + c[::-1])
    
print(heapq.heappop(hq))
        