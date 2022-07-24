all = input()
specific_number = all.split()
a = int(specific_number[0])
b = int(specific_number[1])
c = int(specific_number[2])

print((a+b)%c)

print(((a%c)+(b%c))%c)

print((a*b)%c)

print(((a%c)*(b%c))%c)

