import sys

input = sys.stdin.readline

N, B = map(int, input().split())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))


def mat_mul(a, b, N):
    output = []

    for i in range(N):
        row = []
        for j in range(N):
            count = 0
            for k in range(N):
                count += a[i][k]*b[k][j]
            row.append(count%1000)
        output.append(row)
    return output

count = 1

dp = [matrix]

while 2**count <= B:
    dp.append(mat_mul(dp[-1], dp[-1], N))
    count += 1

output = [[0] * N for _ in range(N)]
for i in range(N):
    output[i][i] = 1

for i, check in enumerate(bin(B)[2:][::-1]):
    if check == '1':
        output = mat_mul(output, dp[i], N)

for row in output:
    for num in row:
        print(num, end=' ')
    print()