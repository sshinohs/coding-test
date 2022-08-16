import sys

input = sys.stdin.readline


for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())

    count = 0
    

    for _ in range(int(input())):
        cx, cy, r = map(int, input().split())

        r1_sqr = (x1 - cx)**2 + (y1 - cy)**2
        r2_sqr = (x2 - cx)**2 + (y2 - cy)**2
        
        r_sqr = r**2

        if (r1_sqr - r_sqr) * (r2_sqr - r_sqr) < 0:
            count += 1
    
    print(count)



