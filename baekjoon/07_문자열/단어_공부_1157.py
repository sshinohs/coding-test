input_str = list(input())

for num, cha in enumerate(input_str):
    if ord(cha)>=97:
        input_str[num] = chr(ord(cha)-32)

final_str = "".join(input_str)

char_num = []
for ii in range(ord('A'), ord('Z')+1):
    char_count = 0
    for jj in final_str:
        if chr(ii) == jj:
            char_count = char_count + 1
    char_num.append(char_count)

max_value = max(char_num)

max_count = 0
for ii, value in enumerate(char_num):
    if char_num[ii] == max_value:
        max_count = max_count + 1
        max_position = ii

if max_count == 1:
    print(chr(ord('A')+max_position))
else:
    print('?')