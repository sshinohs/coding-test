import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

def min_plus_one(arr):
    min_val = min(arr)
    for i in range(len(arr)):
        if arr[i] == min_val:
            arr[i] += 1
    return arr


def first_flying(arr):
    new_arr = []
    new_arr.append(arr[:1])
    new_arr.append(arr[1:])
    arr = new_arr
    return arr

def rotator90(arr):
    len_arr_y = len(arr)
    len_arr_x = len(arr[0])
    new_arr = []
    for i in range(len_arr_x):
        new_arr_row = []
        for j in range(len_arr_y-1, -1, -1):
            new_arr_row.append(arr[j][i])
        new_arr.append(new_arr_row)
    return new_arr

def rotator180(arr):
    len_arr_y = len(arr)
    len_arr_x = len(arr[0])
    new_arr = []
    for j in range(len_arr_y-1, -1, -1):
        new_arr_row = []
        for i in range(len_arr_x-1, -1, -1):
            new_arr_row.append(arr[j][i])
        new_arr.append(new_arr_row)
    return new_arr


def block_splitter_1(arr):
    len_arr_y = len(arr)
    len_arr_x = len(arr[0])
    new_block_arr = []
    new_line_arr = arr[-1][len_arr_x:]
    for i in range(len_arr_y):
        new_block_arr.append(arr[i][:len_arr_x])
    return new_block_arr, new_line_arr


def block_concatenator(a, b):
    a.append(b)
    return a


def stacker_1(arr):
    arr = first_flying(arr)
    while len(arr) <= (len(arr[-1]) - len(arr[0])):
        block, line = block_splitter_1(arr)
        block = rotator90(block)
        arr = block_concatenator(block, line)
    return arr


def check_existence(arr, j, i):
    if j < 0 or j >= len(arr):
        return False
    if i < 0 or i >= len(arr[j]):
        return False
    return True


def fish_transfer(arr):
    neighbor = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    diff_arr = []
    for i in range(len(arr)):
        diff_arr.append(arr[i][:])
    
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            stack = 0
            for neigh in neighbor:
                if check_existence(arr, j+neigh[0], i+neigh[1]):
                    a = arr[j][i]
                    b = arr[j+neigh[0]][i+neigh[1]]
                    diff = abs(a - b) // 5
                    if diff != 0:
                        if a > b:
                            stack -= diff
                        else:
                            stack += diff
            diff_arr[j][i] = stack
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            arr[j][i] += diff_arr[j][i]
    return arr


def liner(arr):
    new_arr = []
    block, line = block_splitter_1(arr)
    
    for i in range(len(block[0])):
        for j in range(len(block)-1, -1, -1):
            new_arr.append(block[j][i])
    
    for num in line:
        new_arr.append(num)
    
    return new_arr


def stacker_2(arr):

    new_arr = []
    new_arr.append(arr[len(arr)//2-1::-1])
    new_arr.append(arr[len(arr)//2:])
    len_arr_y = len(new_arr)
    len_arr_x = len(new_arr[0])

    new_block_a = []
    new_block_b = []

    for j in range(len_arr_y):
        new_block_a.append(new_arr[j][:len_arr_x//2])
        new_block_b.append(new_arr[j][len_arr_x//2:])
    
    new_block_a = rotator180(new_block_a)

    for row in new_block_b:
        new_block_a.append(row)
    return new_block_a


count = 0
while (max(arr) - min(arr)) > K:
    count += 1
    arr = min_plus_one(arr)
    arr = stacker_1(arr)
    arr = fish_transfer(arr)
    arr = liner(arr)
    arr = stacker_2(arr)
    arr = fish_transfer(arr)
    arr = liner(arr)

print(count)