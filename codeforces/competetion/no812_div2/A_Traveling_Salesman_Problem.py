import sys
import math

input = sys.stdin.readline

t = int(input())

for _ in range(t):

    i_max = -math.inf
    i_min = math.inf
    j_max = -math.inf
    j_min = math.inf

    for _ in range(int(input())):
        a, b = map(int, input().split())
        if a > i_max:
            i_max = a
        if a < i_min:
            i_min = a
        if b > j_max:
            j_max = b
        if b < j_min:
            j_min = b
    
    answer = 0
    if i_max >= 0:
        answer += i_max * 2
    if i_min < 0:
        answer -= i_min * 2
    if j_max >= 0:
        answer += j_max * 2
    if j_min < 0:
        answer -= j_min * 2
    
    print(answer)