import sys
input = sys.stdin.readline

while True:
    data = input().strip()
    if data == 'END':
        break
    print(data[::-1])