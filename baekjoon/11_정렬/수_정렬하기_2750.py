num_of_array = int(input())

values = []
for ii in range(num_of_array):
    values.append(int(input()))

finish = False
while(finish==False):
    finish=True
    for ii in range(num_of_array-1):
        if values[ii]>values[ii+1]:
            temp = values[ii+1]
            values[ii+1] = values[ii]
            values[ii] = temp
            finish=False

for value in values:
    print(value)