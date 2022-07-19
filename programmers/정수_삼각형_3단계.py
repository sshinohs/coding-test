def solution(triangle):
    cumul = []
    for row in triangle:
        cumul = [0, *cumul, 0]
        next_cumul = []
        for i in range(len(cumul)-1):
            next_cumul.append(max(cumul[i], cumul[i+1]) + row[i])
        cumul = next_cumul
    answer = max(next_cumul)
    return answer