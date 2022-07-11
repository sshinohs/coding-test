import sys

input = sys.stdin.readline

N, M = map(int, input().split())

trees = list(map(int, input().split()))

max_val = max(trees)

def gain_tree(cut_len):
    count = 0
    for tree in trees:
        count += max(0, tree-cut_len)
    return count

def binary_search(maximum):
    st = 0
    ed = maximum
    
    while True:
        survey = (st + ed) // 2
        check_val = gain_tree(survey)
        if check_val >= M:
            if gain_tree(survey+1) < M:
                return survey
            else:
                st = survey + 1
        else:
            ed = survey - 1


answer = binary_search(max_val)
print(answer)