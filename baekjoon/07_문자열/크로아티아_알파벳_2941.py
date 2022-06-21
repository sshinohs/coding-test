data = input()

len_data = len(data)

count = 0

cur_num = 0
while(cur_num<len_data):
    single_cha = data[cur_num]
    if single_cha == 'c' and cur_num<len_data-1:
        if data[cur_num+1] == '=' or data[cur_num+1] == '-':
            count = count + 1
            cur_num = cur_num + 2
        else:
            count = count + 1
            cur_num = cur_num + 1
    elif single_cha == 'd' and cur_num<len_data-1:
        if cur_num<len_data-2 and data[cur_num+1] == 'z' and data[cur_num+2] =='=':
            count = count + 1
            cur_num = cur_num + 3
        elif data[cur_num+1] == '-':
            count = count + 1
            cur_num = cur_num + 2
        else:
            count = count + 1
            cur_num = cur_num + 1
    elif single_cha == 'l' and cur_num<len_data-1:
        if data[cur_num+1] == 'j':
            count = count + 1
            cur_num = cur_num + 2
        else:
            count = count + 1
            cur_num = cur_num + 1
    elif single_cha == 'n' and cur_num<len_data-1:
        if data[cur_num+1] == 'j':
            count = count + 1
            cur_num = cur_num + 2
        else:
            count = count + 1
            cur_num = cur_num + 1
    elif single_cha == 's' and cur_num<len_data-1:
        if data[cur_num+1] == '=':
            count = count + 1
            cur_num = cur_num + 2
        else:
            count = count + 1
            cur_num = cur_num + 1
    elif single_cha == 'z' and cur_num<len_data-1:
        if data[cur_num+1] == '=':
            count = count + 1
            cur_num = cur_num + 2
        else:
            count = count + 1
            cur_num = cur_num + 1
    else:
        count = count + 1
        cur_num = cur_num + 1

print(count)