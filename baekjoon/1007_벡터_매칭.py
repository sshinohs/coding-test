import sys
import math
from itertools import combinations

input = sys.stdin.readline

for _ in range(int(input())):
    points = []
    N = int(input())
    for _ in range(N):
        points.append(tuple(map(int, input().split())))
    
    min_vector_len_sqr = math.inf

    base_set = list(range(N))
    
    for minus_set in combinations(base_set, N//2):
        cumul = [0, 0]
        for i in range(N):
            if i in minus_set:
                cumul[0] -= points[i][0]
                cumul[1] -= points[i][1]
            else:
                cumul[0] += points[i][0]
                cumul[1] += points[i][1]
        cumul_len_sqr = cumul[0]**2 + cumul[1]**2
        if min_vector_len_sqr > cumul_len_sqr:
            min_vector_len_sqr = cumul_len_sqr
    print(math.sqrt(min_vector_len_sqr))