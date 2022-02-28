input_value = input().split()

a = list(input_value[0])
b = list(input_value[1])

a.reverse()
b.reverse()

a = "".join(a)
b = "".join(b)

if a>b:
    print(a)
else:
    print(b)