data = input()

len_data = len(data)

for ii in range(97,123):
    is_exist = 0
    for jj in range(len_data):
        if ii == ord(data[jj]):
            print(jj, end='')
            print(" ", end='')
            is_exist = 1
            break
    if is_exist == 0:
        print(-1,end='')
        print(" ", end='')
print()
