import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    data = list(map(int, input().split()))[::-1]

    zero_set = set()

    min_value = 10**5+1

    end_idx = len(data)

    flag = True

    while flag:
        for i, num in enumerate(data[:end_idx]):
            if num in zero_set:
                min_value = 0
            elif min_value >= num:
                min_value = num
            else:
                zero_set = zero_set.union(set(data[i:]))
                end_idx = i
                min_value = 10**5+1
                break
        else:
            flag = False
    print(len(zero_set))