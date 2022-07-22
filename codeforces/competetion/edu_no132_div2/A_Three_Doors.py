import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    key_on_hand = int(input())
    data_in_the_rooms = list(map(int, input().split()))
    
    now = key_on_hand - 1
    for _ in range(2):
        nxt = data_in_the_rooms[now]
        if nxt == 0:
            print('NO')
            break
        else:
            now = nxt - 1
    else:
        print('YES')