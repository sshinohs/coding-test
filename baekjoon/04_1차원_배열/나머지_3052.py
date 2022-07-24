size_of_input = 10

divider = 42

remainder = []

for ii in range(10):
    num = int(input())
    remainder.append(num%divider)

unique = 0

for idx, num in enumerate(remainder):
    criteria = 1
    for ii in range(idx):
        if remainder[ii] == num:
            criteria = 0
    unique = unique + criteria

print(unique)