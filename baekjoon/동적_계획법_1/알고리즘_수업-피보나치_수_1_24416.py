num = int(input())

def fibonacci(n, arr):
    arr.append(0)
    arr.append(1)
    arr.append(1)
    count = 0
    for i in range(3, n+1):
        count += 1
        arr.append(arr[i-2] + arr[i-1])
    
    return arr[n], count



arr = []
ham = fibonacci(num, arr)

print(ham[0], end=' ')
print(ham[1])

