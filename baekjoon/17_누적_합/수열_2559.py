import sys
input = sys.stdin.readline

N, K = map(int, input().split())

nums = list(map(int, input().split()))

cumul = [sum(nums[:K])]

for i in range(N-K):
    cumul.append(cumul[-1] - nums[i] + nums[i+K])

print(max(cumul))