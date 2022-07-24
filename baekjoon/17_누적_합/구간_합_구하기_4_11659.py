import sys

N, M = list(map(int, sys.stdin.readline().split()))

nums = list(map(int, sys.stdin.readline().split()))

cumulative_sum = [0]

for i in nums:
    cumulative_sum.append(cumulative_sum[-1]+i)


# answer = []

for i in range(M):
    st, ed = list(map(int, sys.stdin.readline().split()))
    print(cumulative_sum[ed]-cumulative_sum[st-1])

# for ans in answer:
#     print(ans)