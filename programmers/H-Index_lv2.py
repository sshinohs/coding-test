def solution(citations):
    citations = sorted(citations)
    len_cite = len(citations)
    
    
    h = 0
    while True:
        if len_cite == h:
            return len_cite
        if citations[len_cite-h-1] <= h:
            break
        else:
            h += 1
    answer = h
    return answer


def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0