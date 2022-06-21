a = int(input())
b = int(input())
c = int(input())

result = a*b*c

result_str = str(result)

for ii in range(10):
    number = 0
    for jj in result_str:
        if str(ii)==jj:
            number = number+1
    print(number)