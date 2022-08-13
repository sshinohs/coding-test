import sys

input = sys.stdin.readline

X = int(input())

count = 0

cumul = 0

while cumul < X:
    count += 1
    cumul += count

cumul -= count

order = X - cumul

denominator = order

numerator = count + 1 - denominator

if count % 2 == 1:
    print(numerator, end = '')
    print('/', end='')
    print(denominator)
else:
    print(denominator, end = '')
    print('/', end='')
    print(numerator)
