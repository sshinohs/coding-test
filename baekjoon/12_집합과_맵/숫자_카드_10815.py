


# a = "5"
# b = "6 3 2 10 -10"
# c = "8"
# d = "10 9 -5 2 3 4 5 -10"

a = input()
b = input()
c = input()
d = input()



a = int(a)
b = list(map(int, b.split(' ')))
c = int(c)
d = list(map(int, d.split(' ')))

num_set = {}

for i in b:
    if i not in num_set:
        num_set[i] = 1

for i in d:
    if i in num_set:
        print('1 ', end='')
    else:
        print('0 ', end='')