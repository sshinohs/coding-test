case_num = int(input())

for ii in range(case_num):
    data = input().split()
    iter_num = int(data[0])
    data_str = data[1]
    
    for jj in data_str:
        for kk in range(iter_num):
            print(jj, end='')

    print()