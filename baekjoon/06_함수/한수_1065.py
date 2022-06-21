last_num = int(input())

hansu_count = 0
for num in range(1,last_num+1):

    num_str = str(num)
    len_num = len(num_str)

    hansu = 1
    if len_num>2:
        for jj in range(len_num-2):
            if int(num_str[jj]) - int(num_str[jj+1]) != int(num_str[jj+1]) - int(num_str[jj+2]):
                hansu = 0
    
    hansu_count = hansu_count + hansu

print(hansu_count)