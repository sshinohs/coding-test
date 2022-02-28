input_cha = input()

dial_num = []
for single_cha in input_cha:
    if single_cha =='A' or single_cha =='B' or single_cha =='C':
        dial_num.append(2)
    elif single_cha =='D' or single_cha =='E' or single_cha =='F':
        dial_num.append(3)
    elif single_cha =='G' or single_cha =='H' or single_cha =='I':
        dial_num.append(4)
    elif single_cha =='J' or single_cha =='K' or single_cha =='L':
        dial_num.append(5)
    elif single_cha =='M' or single_cha =='N' or single_cha =='O':
        dial_num.append(6)
    elif single_cha =='P' or single_cha =='Q' or single_cha =='R' or single_cha =='S':
        dial_num.append(7)
    elif single_cha =='T' or single_cha =='U' or single_cha =='V':
        dial_num.append(8)
    elif single_cha =='W' or single_cha =='X' or single_cha =='Y' or single_cha =='Z':
        dial_num.append(9)

time_num = []
for single_num in dial_num:
    time_num.append(single_num+1)

total_time = 0

for one_time in time_num:
    total_time = total_time + one_time

print(total_time)