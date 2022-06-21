size_of_array = 9

a = []

for ii in range(size_of_array):
    a.append(int(input()))

max_value = max(a)
max_index = a.index(max_value)
print(max_value)
print(max_index+1)