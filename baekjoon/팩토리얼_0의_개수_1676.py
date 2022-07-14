import sys

input = sys.stdin.readline

N = int(input())

def factorial(n):
    if n == 0:
        return 1
    output = 1
    for i in range(1,n+1):
        output *= i
    return output

result = str(factorial(N))[::-1]
# print(result)

for i, cha in enumerate(result):
    if cha != '0':
        print(i)
        break