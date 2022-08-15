import sys

input = sys.stdin.readline

data = input().strip()

total = []
x_len = 0
flag = False
for cha in data:
    if cha == '.':
        if x_len > 0:
            if x_len % 2 == 1:
                flag = True
            else:
                total.append((x_len // 4) * 'AAAA')
                total.append((x_len % 4) * 'B')
                x_len = 0
        total.append('.')
    else:
        x_len += 1

if x_len > 0:
    if x_len % 2 == 1:
        flag = True
    else:
        total.append((x_len // 4) * 'AAAA')
        total.append((x_len % 4) * 'B')
if flag:
    print(-1)
else:
    print(''.join(total))