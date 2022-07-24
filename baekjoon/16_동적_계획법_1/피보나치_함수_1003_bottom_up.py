last_num = 41
fibo = [0]*last_num

fibo[0] = 0
fibo[1] = 1

for ii in range(2,last_num):
    fibo[ii] = fibo[ii-2]+fibo[ii-1]

fibo.insert(0,1)
# print(fibo)

case_num = int(input())

for ii in range(case_num):
    input_num = int(input())
    print(' '.join(map(str, fibo[input_num:input_num+2])))