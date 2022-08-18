import sys
input = sys.stdin.readline

for _ in range(int(input())):

    n, m = map(int, input().split())

    before = []
    flag = False
    flag2 = True
    count = 0
    for _ in range(n):
        nxt = []
        left = False
        for i, num in enumerate(map(int, list(input().strip()))):
            count += num
            if flag2:
                if num == 0:
                    flag = True
                    nxt.append(i)
                    if i in before or i-1 in before or i+1 in before or left:
                        check = 0
                        flag2 = False
                    left = True
                else:
                    left = False
        before = nxt
    if flag2:
        if flag:
            check = 1
        else:
            check = 2
        
    print(count - check)
        
    