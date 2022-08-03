def solution(n, times):
    times.sort()
    max_time = round(n/len(times))*times[-1]
    
    answer = binary_search(times, 1, max_time, max_time, n)
    return answer

def binary_search(arr, st, ed, tmp, target):
    if st > ed:
        return tmp
    mid = (st + ed) // 2
    check = people_calculator(mid, arr)
    if check >= target:
        tmp = mid
        ed = mid - 1
    else:
        st = mid + 1
    return binary_search(arr, st, ed, tmp, target)

def people_calculator(criteria, times):
    count = 0
    for time in times:
        count += criteria // time
    return count