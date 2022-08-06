import sys

input = sys.stdin.readline

capacity = 5

luggages = list(map(int, input().split()))

bag_num = 0
while sum(luggages) > 0:
    bag_num += 1
    count = 0
    for i in range(capacity, 0, -1):
        while luggages[i-1] > 0 and count + i <= capacity:
            count += i
            luggages[i-1] -= 1

print(bag_num)