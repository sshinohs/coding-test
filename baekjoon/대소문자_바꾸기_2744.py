import sys

input = sys.stdin.readline

data = input()[:-1]

answer = ''

for cha in data:
    if ord(cha) >= ord('a') and ord(cha) <= ord('z'):
        answer += chr(ord(cha) + ord('A') - ord('a'))
    else:
        answer += chr(ord(cha) + ord('a') - ord('A'))

print(answer)