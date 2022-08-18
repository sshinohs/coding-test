import sys
import math
input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    ad = a*d
    bc = b*c
    if ad == bc:
        print(0)
    else:
        num_gcd = math.gcd(ad, bc)
        if num_gcd == ad or num_gcd == bc:
            print(1)
        else:
            print(2)