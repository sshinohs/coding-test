from itertools import permutations

def solution(k, dungeons):
    orders = list(permutations([i for i in range(len(dungeons))], len(dungeons)))
    max_count = 0
    for order in orders:
        check = simulator(k, dungeons, order)
        if check > max_count:
            max_count = check
    answer = max_count
    return answer

def simulator(k, dungeons, order):
    count = 0
    for now in order:
        if k >= dungeons[now][0]:
            count += 1
            k -= dungeons[now][1]
        else:
            break
    return count