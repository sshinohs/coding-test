import sys

input = sys.stdin.readline

arr = [0, 1, 2, 4]

def one_two_three(n):
    if n < len(arr):
        return arr[n]
    else:
        for i in range(len(arr), n+1):
            arr.append(arr[i-3] + arr[i-2] + arr[i-1])
    return arr[n]

T = int(input())

for _ in range(T):
    N = int(input())
    print(one_two_three(N))