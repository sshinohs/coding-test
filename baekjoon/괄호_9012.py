import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    parenthesis = input()

    count = 0

    for paren in parenthesis:
        if paren == '(':
            count += 1
        elif paren == ')':
            count -= 1
        
        if count < 0:
            answer = 'NO'
            break
    
    if count == 0:
        answer = 'YES'
    else:
        answer = 'NO'

    print(answer)