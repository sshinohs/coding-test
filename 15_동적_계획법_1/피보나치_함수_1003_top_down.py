
global count_zero
count_zero = 0
global count_one
count_one = 0

num = int(input())

def fibonacci(n):
    global count_zero
    global count_one
    if n==0:
        count_zero = count_zero + 1
        return 0
    elif n==1:
        count_one = count_one + 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(num)
print(count_zero)
print(count_one)