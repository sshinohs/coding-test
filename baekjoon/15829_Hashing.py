import sys
input = sys.stdin.readline

L = int(input())

data = list(input())

def hashing(data):
    output = 0
    for i, cha in enumerate(data):
        output += (ord(cha)-ord('a')+1)*31**i
    output %= 1234567891
    return output

print(hashing(data[:-1]))