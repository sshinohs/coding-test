import sys

input = sys.stdin.readline

def padovan_arr(n):
    arr = [0, 1, 1, 1, 2, 2]
    if n <= 5:
        return arr[n]
    for _ in range(5, n):
        arr.append(arr[-1] + arr[-5])
    return arr

n_max = 100

T = int(input())

padovans = padovan_arr(100)

for _ in range(T):
    print(padovans[int(input())])