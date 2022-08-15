import sys
 
input = sys.stdin.readline
 
for _ in range(int(input())):
    n = int(input())
 
    num_set = set()
 
    zero_num_set = set()
    
    max_num = 0
 
    for num in map(int, input().split()):
        if max_num <= num and num not in zero_num_set:
            max_num = num
            num_set.add(num)
        else:
            max_num = num
            zero_num_set = zero_num_set.union(num_set)
            num_set = set([num])
    print(len(zero_num_set))
