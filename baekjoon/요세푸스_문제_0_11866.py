import sys
input = sys.stdin.readline

N, K = map(int, input().split())

peoples = [i+1 for i in range(N)]

count = -1

# print(peoples)

print('<', end='')
while len(peoples) > 1:
    count += K
    while count >= len(peoples):
        count -= len(peoples)
    print(peoples.pop(count), end='')
    count -= 1
    print(', ', end='')

print(peoples[0], end='')
print('>')