num_loop = int(input())

for ii in range(1, num_loop+1):
    for kk in range(num_loop-ii):
        print(' ', end='')
    for jj in range(ii):
        print('*', end='')
    print()