import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    n, q = map(int, input().split())
    participants = list(range(1, n+1))
    strengths = list(map(int, input().split()))
    dq = deque(list(zip(participants, strengths)))
    scores = [[(0, 0)] for _ in range(n+1)]
    powerful = strengths.index(max(strengths))
    for round in range(1, powerful+1):
        a = dq.popleft()
        b = dq.popleft()
        if a[1] > b[1]:
            scores[a[0]].append((round, scores[a[0]][-1][1]+1))
            dq.appendleft(a)
            dq.append(b)
        else:
            scores[b[0]].append((round, scores[b[0]][-1][1]+1))
            dq.appendleft(b)
            dq.append(a)
    for _ in range(q):
        i, k = map(int, input().split())
        max_value = 0
        for record in scores[i]:
            if record[0] > k:
                break
            max_value = record[1]

        if k > powerful:
            if i == powerful + 1:
                if powerful == 0:
                    print(k)
                else:
                    print(k-powerful+1)
            else:
                print(max_value)
        else:
            print(max_value)