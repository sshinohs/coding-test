import sys

input = sys.stdin.readline

val = input()

num = int(val)

minimum = num - (int(val[0])+9*(len(val)-2))

for i in range(minimum, num):
    temp = list(str(i))
    test_val = i
    for j in temp:
        test_val += int(j)
    if test_val == num:
        print(i)
        break
else:
    print(0)

# a = '123'

# print(a.split(''))