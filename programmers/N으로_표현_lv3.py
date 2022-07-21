def solution(N, number):
    sheet = [set([0])]
    sheet.append(set([N]))
    if N == number:
        return 1
    for i in range(2, 9):
        next_set = set()
        next_set.add(int(str(N)*i))
        for a in range(1, i):
            b = i - a
            for m in sheet[a]:
                for n in sheet[b]:
                    next_set.add(m + n)
                    next_set.add(m - n)
                    next_set.add(m * n)
                    if n != 0:
                        next_set.add(m // n)
        if number in next_set:
            return i
        sheet.append(next_set)
    return -1

print(solution(5, 12))