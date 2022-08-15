import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())

min_cost = math.inf

min_pac = math.inf
min_one = math.inf

for _ in range(M):
    pac_cost, one_cost = map(int, input().split())
    if min_pac > pac_cost:
        min_pac = pac_cost
    if min_one > one_cost:
        min_one = one_cost

all_pac_cost = math.ceil(N / 6) * min_pac
all_one_cost = N * min_one
mix_cost = N//6 * min_pac + N%6 * min_one
print(min(all_pac_cost, all_one_cost, mix_cost))
    