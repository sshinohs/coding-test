import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    print(n, end = ' ')
    for i in range(1, n):
        print(i, end=' ')
    print()
    




## 참고 2 by hsh8086
# import sys
# input = lambda: sys.stdin.readline().rstrip()
 
# for _ in range(int(input())):
#     n = int(input())
 
#     r = []
#     if n % 2 == 0:
#         for i in range(0, n, 2):
#             r.append(i + 2)
#             r.append(i + 1)
#     else:
#         r.append(1)
#         for i in range(1, n, 2):
#             r.append(i + 2)
#             r.append(i + 1)
 
 
#     print(*r)



## 참고 1 by swoon
# import sys
 
# R = lambda : sys.stdin.readline()
# MIS = lambda : map(int, R().split())
 
# for _ in range(int(R())):
#     N = int(R())
#     if N&1:
#         print(1, end=" ")
#         for i in range(2, N+1, 2):
#             print(i+1, i, end=" ")
#     else:
#         for i in range(1, N+1, 2):
#             print(i+1, i, end=" ")
#     print()
