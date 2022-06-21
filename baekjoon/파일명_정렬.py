def solution(files):
    bubble_sort_for_files(files)
    return files

def bubble_sort_for_files(arr):
    flag = 1
    while flag == 1:
        flag = 0
        for i in range(len(arr)-1):
            head_a, st_a = extract_head(arr[i])
            head_b, st_b = extract_head(arr[i+1])
            head_check = swap_head(head_a, head_b)
            if  head_check == 1:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = 1
            elif head_check == 0:
                number_a = extract_number(arr[i], st_a)
                number_b = extract_number(arr[i+1], st_b)
                number_check = swap_number(number_a, number_b)
                if number_check == 1:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    flag = 1


def swap_number(number_a, number_b):
    a = int(number_a)
    b = int(number_b)
    # print(number_a + ' ' + number_b)
    if a == b:
        return 0
    if a > b:
        # print(str(a) + ' ' + str(b))
        return 1
    else:
        return 2                    
                    
def swap_head(head_a, head_b):
    temp = [head_a.upper(), head_b.upper()]
    if temp[0] == temp[1]:
        return 0
    temp.sort()
    if temp[0] != head_a.upper():
        # print(temp)
        return 1
    else:
        return 2
                

def extract_number(fn, st):
    count = 1
    limit_fn = len(fn)
    while is_num(fn[st+count]):
        count += 1
        if st+count == limit_fn:
            break
        if count == 5:
            break
    return fn[st:st+count]
                
def extract_head(fn):
    count = 1
    while is_num(fn[count]) == False:
        count += 1
    return fn[:count], count

def is_num(cha):
    if ord(cha) >= ord('0') and ord(cha) <= ord('9'):
        return True
    return False