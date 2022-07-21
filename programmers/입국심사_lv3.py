def solution(n, times):
    times.sort()
    max_time = round(n/len(times))*times[-1]
    
    answer = binary_search(times, 1, max_time, n)
    return answer

def binary_search(arr, st, ed, target):
    tmp = ed
    left = st
    right = ed
    while left <= right:
        mid = (left + right) // 2
        check = people_calculator(mid, arr)
        if check >= target:
            tmp = mid
            right = mid - 1
        else:
            left = mid + 1
    return tmp

def people_calculator(criteria, times):
    count = 0
    for time in times:
        count += criteria // time
    return count