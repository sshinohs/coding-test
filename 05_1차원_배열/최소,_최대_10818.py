size_of_array = int(input())

data = input().split()

a = []

for num in range(size_of_array):
    a.append(int(data[num]))

value_max = max(a)
value_min = min(a)

print(str(value_min) + " " + str(value_max))