
import sys

input = sys.stdin.readline

for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())

    t1 = h1 * 60 **2 + m1 * 60 + s1
    t2 = h2 * 60 **2 + m2 * 60 + s2
    
    t = t2 - t1

    print(t // 60 ** 2, (t % 60**2) // 60, t % 60)