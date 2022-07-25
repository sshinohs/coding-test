import math

def solution(arr):
    len_arr = len(arr)
    count = 0
    nums  = []
    opers = []
    while count < len_arr-1:
        nums.append(int(arr[count]))
        opers.append(arr[count+1])
        count += 2
    nums.append(int(arr[count]))
    len_nums = len(nums)
    len_opers = len(opers)
    
    dp = [[[math.inf]*2 for _ in range(len_opers+1)] for _ in range(len_opers+1)]
    
    [total_max, total_min] = dp_func(dp, nums, opers, 0, len_opers)
    answer = total_max
    return answer

def dp_func(dp, nums, opers, left, right):
    
    if dp[left][right][0] == math.inf:
        if left == right:
            dp[left][right] = [nums[left], nums[left]]
        else:
            max_val = -math.inf
            min_val = math.inf
            for i in range(left, right):
                [l_max, l_min] = dp_func(dp, nums, opers, left, i)
                [r_max, r_min] = dp_func(dp, nums, opers, i+1, right)
                if opers[i] == '+':
                    check_max = l_max + r_max
                    check_min = l_min + r_min
                else:
                    check_max = l_max - r_min
                    check_min = l_min - r_max
                if max_val < check_max:
                    max_val = check_max
                if min_val > check_min:
                    min_val = check_min
            dp[left][right] = [max_val, min_val]
    
    return dp[left][right]