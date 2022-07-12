import sys

input = sys.stdin.readline

N, M = map(int, input().split())

def factorial_arr(n):
    output_arr = [1]
    if n == 0:
        return output_arr
    for i in range(1, n+1):
        output_arr.append(output_arr[-1] * i)
    return output_arr

fact_arr = factorial_arr(N)

print(fact_arr[N]//fact_arr[M]//fact_arr[N-M])