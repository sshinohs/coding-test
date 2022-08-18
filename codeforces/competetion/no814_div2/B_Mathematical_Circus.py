import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    if k % 2 == 1:
        print('YES')
        for i in range(1, n+1, 2):
                print(i, i+1)
    elif (k+2)%4 == 0:
        print('YES')
        for i in range(3, n+1, 4):
            print(i, i+1)
        for i in range(1, n+1, 4):
            print(i+1, i)
    else:
        print('NO')