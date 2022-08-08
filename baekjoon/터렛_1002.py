import sys

input = sys.stdin.readline


for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist_ab = (y2-y1)**2+(x2-x1)**2
    dist_target_sum = (r1 + r2)**2
    if dist_ab == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif dist_ab > dist_target_sum:
        print(0)
    elif dist_ab == dist_target_sum:
        print(1)
    elif abs(r1-r2)**2 > dist_ab:
        print(0)
    elif abs(r1-r2)**2 == dist_ab:
        print(1)
    else:
        print(2)
    
