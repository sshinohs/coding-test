number_of_case = int(input())

for ii in range(number_of_case):
    
    data_sheet = input().split()
    number_of_class = int(data_sheet[0])

    sum = 0
    for jj in range(number_of_class):
        sum = sum + int(data_sheet[jj+1])
    
    score_average = sum/number_of_class

    more_than_average = 0
    for jj in range(number_of_class):
        if int(data_sheet[jj+1])>score_average:
            more_than_average = more_than_average+1
    
    output_value = more_than_average/number_of_class*100
    print("{0:.3f}%".format(output_value))
