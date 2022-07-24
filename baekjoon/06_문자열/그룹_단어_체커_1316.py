number_of_case = int(input())

group_count = 0

for ii in range(number_of_case):
    is_group = 1
    word = input()
    cha_archive = []
    cha_before = ' '
    for cha_single in word:
        if cha_single not in cha_archive or cha_before == cha_single:
            cha_archive.append(cha_single)
            cha_before = cha_single
        else:
            is_group = 0
    group_count = group_count + is_group

print(group_count)