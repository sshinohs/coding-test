def solution(routes):
    routes.sort(key = lambda x : x[1])
    answer = 1
    check = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] > check:
            answer += 1
            check = routes[i][1]
    return answer