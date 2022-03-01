input_num = int(input())

data = input().split()

count = 0
for value in data:
    num = int(value)
    if num == 1:
        is_prime = 0
    else:
        is_prime = 1
    for ii in range(2, num):
        if num%ii==0:
            is_prime = 0
    count = count + is_prime

print(count)