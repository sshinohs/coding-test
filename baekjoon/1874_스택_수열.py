import sys
input = sys.stdin.readline

n = int(input())

nxt = 0

stack = []

result = []

flag = False

for _ in range(n):
    num = int(input())
    while nxt < num:
        nxt += 1
        stack.append(nxt)
        result.append('+')
        # print(result)
        # print(stack)
    if num == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        flag = True


if flag:
    print('NO')
else:
    for output in result:
        print(output)