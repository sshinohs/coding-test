import sys

input = sys.stdin.readline

n = int(input())

root = int(input())

if n == 1:
    print(root)
else:
    cumul = [[root]]
    for i in range(1, n):
        nums = list(map(int, input().split()))
        # print(nums)
        # print(cumul)
        cumul_row = [cumul[i-1][0]+nums[0]]
        for j in range(1, len(nums)-1):
            cumul_row.append(max(cumul[i-1][j-1], cumul[i-1][j])+nums[j])
        cumul_row.append(cumul[i-1][-1]+nums[-1])
        cumul.append(cumul_row)
    print(max(cumul_row))