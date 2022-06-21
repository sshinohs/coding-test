import math

data = input().split()

a = int(data[0])
b = int(data[1])
c = int(data[2])


try:
    result = math.floor(a/(c-b))+1
    if result > 0 :
        print(result)
    else:
        print(-1)
except:
    print(-1)