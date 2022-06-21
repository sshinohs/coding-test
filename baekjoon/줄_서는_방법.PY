def solution(n, k):
    count = [0]
    answer = []
    nums = [1 for i in range(n)]
    facto = factorial(n)
    lineup(facto, answer, nums, count, k)
    return answer

def lineup(facto, lines, nums, count, k):
    check = sum(nums)
    st = 0
    
    if sum(nums) == 0:
        count[0] += 1
    else:
        while k < count[0]+facto[check-1]:
            st += 1
            count[0] += facto[check-1]
        for i in range(st, len(nums)):
            if nums[i] == 1:
                lines.append(i+1)
                nums[i] = 0
                lineup(facto, lines, nums, count, k)
                if count[0] == k:
                    return
                lines.pop()
                nums[i] = 1

def factorial(n):
    fact_arr = [1]
    for i in range(1,n+1):
        fact_arr.append(fact_arr[i-1]*(i))
    return fact_arr