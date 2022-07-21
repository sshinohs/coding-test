import sys

def LCM(a, b):
    while True:
        # print(a, b)
        if a > b:
            temp = b
            b = a
            a = temp
        check = b % a
        if check == 0:
            return a
        else:
            b = check

def GCD(a, b):
    lcm = LCM(a, b)
    return a * b // lcm

input = sys.stdin.readline


def finder(m, n, x, y):
    gcd = GCD(m, n)
    count_m = 0
    count_n = 0
    while count_m * m <= gcd and count_n * n <= gcd:
        a = count_m * m + x
        b = count_n * n + y
        if a == b:
            return a
        elif a > b:
            count_n += 1
        elif a < b:
            count_m += 1
    return -1

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(finder(M, N, x, y))


