# arr = [1,2,3,3,3,3,4,4]
# arr = [3,2,4,4,2,5,2,5,5]
arr = [3,5,7,9,1]



answer = []

arr.sort()

check = arr[0]
count = 0
for i in range(1,len(arr)):
    if arr[i] == check:
        count += 1
    else:
        if count > 0:
            answer.append(count+1)
            count = 0
        check = arr[i]

if count > 0:
    answer.append(count+1)
    count = 0

if len(answer) == 0:
    print([-1])
else:
    print(answer)