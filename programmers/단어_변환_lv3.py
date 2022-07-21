from collections import deque

def solution(begin, target, words):
    
    len_words = len(words)
    
    q = deque()
    
    visited = [0] * len_words
    
    for i in range(len_words):
        if word_convertible(begin, words[i]):
            q.append((words[i], i))
            visited[i] = 1
    
    while q:
        now = q.popleft()
        if now[0] == target:
            return visited[now[1]]
        for i in range(len_words):
            if visited[i] == 0:
                if word_convertible(now[0], words[i]):
                    q.append((words[i], i))
                    visited[i] = visited[now[1]] + 1
    return 0

def word_convertible(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False