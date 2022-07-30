import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    if n == 0:
        print(0)
    else:  
        items_dict = {}
        for _ in range(n):
            item, category = input().rstrip().split()
            if category not in items_dict:
                items_dict[category] = 1
            else:
                items_dict[category] += 1
        count = 1
        for item in items_dict:
            count *= items_dict[item]+1
        print(count - 1)
    