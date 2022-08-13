import sys
input = sys.stdin.readline

n = int(input())

arr = [0, 1, 2]

if n < 2:
    print(arr[n]%10007)
else:
    for i in range(3, n+1):
        arr.append(arr[i-2]+arr[i-1])
    print(arr[n]%10007)