import sys

input = sys.stdin.readline

N = int(input())

sheet = []
for _ in range(N):
    sheet.append(list(map(int, input().split())))

# st = N//2

diff = [(0, -1), (1, 0), (0, 1), (-1, 0)]
diff_1 = [(0, -1), (1, 0)]
diff_2 = [(0, 1), (-1, 0)]

yp = N//2
xp = N//2

spread_percent = [
    [[0, 0, 2, 0, 0], [0, 10, 7, 1, 0], [5, 0, 0, 0, 0], [0, 10, 7, 1, 0], [0, 0, 2, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [2, 7, 0, 7, 2], [0, 10, 0, 10, 0], [0, 0, 5, 0, 0]],
    [[0, 0, 2, 0, 0], [0, 1, 7, 10, 0], [0, 0, 0, 0, 5], [0, 1, 7, 10, 0], [0, 0, 2, 0, 0]],
    [[0, 0, 5, 0, 0], [0, 10, 0, 10, 0], [2, 7, 0, 7, 2], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]],
]


def make_spread(sand_amount, direction):
    spreaded = []
    for row in spread_percent[direction]:
        spreaded_row = []
        for percent in row:
            spreaded_row.append(int(sand_amount * percent / 100))
        spreaded.append(spreaded_row)
    
    total_spreaded = sum(map(sum, spreaded))
    spreaded[2 + diff[direction][0]][2 + diff[direction][1]] += (sand_amount - total_spreaded)

    return spreaded


def check_valid_idx(y, x):
    if y < 0 or y >= N or x < 0 or x >= N:
        return False
    return True


out_amount = 0

toggle = True
for i in range(1, N):
    if toggle:
        for direc, dif in enumerate(diff_1):
            direction = direc
            for _ in range(i):
                yp += dif[0]
                xp += dif[1]
                sand_amount = sheet[yp][xp]
                spreaded = make_spread(sand_amount, direction)
                for yy in range(len(spreaded)):
                    for xx in range(len(spreaded[0])):
                        diff_y = yy-2
                        diff_x = xx-2

                        target_y = diff_y + yp
                        target_x = diff_x + xp
                        
                        if check_valid_idx(target_y, target_x):
                            sheet[target_y][target_x] += spreaded[yy][xx]
                        else:
                            out_amount += spreaded[yy][xx]
                sheet[yp][xp] = 0
                
    else:
        for direc, dif in enumerate(diff_2):
            direction = direc + 2
            for _ in range(i):
                yp += dif[0]
                xp += dif[1]
                sand_amount = sheet[yp][xp]
                spreaded = make_spread(sand_amount, direction)
                for yy in range(len(spreaded)):
                    for xx in range(len(spreaded[0])):
                        diff_y = yy-2
                        diff_x = xx-2

                        target_y = diff_y + yp
                        target_x = diff_x + xp
                        
                        if check_valid_idx(target_y, target_x):
                            sheet[target_y][target_x] += spreaded[yy][xx]
                        else:
                            out_amount += spreaded[yy][xx]
                sheet[yp][xp] = 0
    toggle = not toggle


direction = 0
dif = diff_1[0]
for _ in range(1, N):
    yp += dif[0]
    xp += dif[1]
    sand_amount = sheet[yp][xp]
    spreaded = make_spread(sand_amount, direction)
    for yy in range(len(spreaded)):
        for xx in range(len(spreaded[0])):
            diff_y = yy-2
            diff_x = xx-2

            target_y = diff_y + yp
            target_x = diff_x + xp
            
            if check_valid_idx(target_y, target_x):
                sheet[target_y][target_x] += spreaded[yy][xx]
            else:
                out_amount += spreaded[yy][xx]
    sheet[yp][xp] = 0
print(out_amount)
