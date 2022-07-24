info = map(int, input().split(' '))

# info = [6, 2, 10, 3]
# info = [1, 1, 5, 5]
# info = [653, 375, 1000, 1000]

x, y, w, h = info

min_distance = x

if w-x < min_distance:
    min_distance = w-x

if y < min_distance:
    min_distance = y

if h-y < min_distance:
    min_distance = h-y

print(min_distance)