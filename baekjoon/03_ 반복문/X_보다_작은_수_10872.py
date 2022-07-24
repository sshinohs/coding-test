meta = input()
numbers = meta.split()
size_of_array = int(numbers[0])
criteria = int(numbers[1])

data_str = input()
data_all = data_str.split()

for data in data_all:
    if int(data) < criteria :
        print(data+" ", end='')

print()