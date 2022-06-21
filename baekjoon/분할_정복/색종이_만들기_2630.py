import sys

size = int(sys.stdin.readline())

arr = []

for _ in range(size):
    arr.append(list(map(int, sys.stdin.readline().split())))


# arr = [[1, 1, 0, 0, 0, 0, 1, 1],
#     [1, 1, 0, 0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 1, 1, 0, 0],
#     [0, 0, 0, 0, 1, 1, 0, 0],
#     [1, 0, 0, 0, 1, 1, 1, 1],
#     [0, 1, 0, 0, 1, 1, 1, 1],
#     [0, 0, 1, 1, 1, 1, 1, 1],
#     [0, 0, 1, 1, 1, 1, 1, 1]]

# arr = [[1]]

# size = 8

def divider(arr, y1, x1, y2, x2):
    # print('$$')
    # print([y1, x1])
    # print([y2, x2])

    total = 0

    for i in range(y1, y2):
        total += sum(arr[i][x1:x2])
    
    # print(total)
    num_one = 0
    num_zero = 0
    if total == (y2-y1)**2:
        num_one = 1
    elif total == 0:
        num_zero = 1
    else:
        temp_one, temp_zero = divider(arr, y1, x1, y1+(y2-y1)//2, x1+(x2-x1)//2)
        num_one += temp_one
        num_zero += temp_zero
        temp_one, temp_zero = divider(arr, y1, x1+(x2-x1)//2, y1+(y2-y1)//2, x2)
        num_one += temp_one
        num_zero += temp_zero
        temp_one, temp_zero = divider(arr, y1+(y2-y1)//2, x1, y2, x1+(x2-x1)//2)
        num_one += temp_one
        num_zero += temp_zero
        temp_one, temp_zero = divider(arr, y1+(y2-y1)//2, x1+(x2-x1)//2, y2, x2)
        num_one += temp_one
        num_zero += temp_zero
    # print([num_one, num_zero])
    # print('@@@')
    return num_one, num_zero


num_one, num_zero = divider(arr, 0, 0, size, size)

# divider(arr, 0, 0, size, size)

print(num_zero)
print(num_one)
