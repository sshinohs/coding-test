data = input().split()

max_val = int(data[0])
max_pos = int(data[1])-1

cur_array = []

for ii in range(max_pos):
    cur_array.append(1)

cur_array.append(0)

cur_pos = max_pos

def add_man(cur_array, max_val, cur_pos, max_pos):
    if cur_array[cur_pos] < max_val:
        cur_array[cur_pos] = cur_array[cur_pos]+1
        print_if(cur_array, max_val)
        add_man(cur_array, max_val, max_pos, max_pos)
    elif cur_pos == 0:
        return 0
    else:
        cur_array[cur_pos] = 1
        add_man(cur_array, max_val, cur_pos-1, max_pos)

def print_if(cur_array, max_val):
    for ii in range(1, max_val+1):
        count = 0
        for cur_val in cur_array:
            if cur_val == ii:
                count = count + 1
        if count > 1:
            return 0
    print_man(cur_array)

def print_man(cur_array):
    for cur_val in cur_array:
        print(cur_val, end='')
        print(' ',end='')
    print()


add_man(cur_array, max_val, cur_pos, max_pos)