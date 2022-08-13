import sys

input = sys.stdin.readline

n = int(input())

eschatology_num = []
count = 0
for _ in range(n):
    while True:
        count += 1
        if '666' in str(count):
            eschatology_num.append(count)
            break
        

print(eschatology_num[-1])