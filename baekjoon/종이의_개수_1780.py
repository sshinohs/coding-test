import sys

input = sys.stdin.readline

N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

yr = (0, N)
xr = (0, N)

def check(yr, xr):
    check_num = sum([sum(row[xr[0]:xr[1]]) for row in board[yr[0]:yr[1]]])
    
    check_num = board[yr[0]][xr[0]]
    flag = True
    for row in board[yr[0]:yr[1]]:
        for element in row[xr[0]:xr[1]]:
            if element != check_num:
                flag = False
                break
        if flag == False:
            break
    
    if flag:
        if check_num == -1:
            return [1, 0, 0]
        elif check_num == 0:
            return [0, 1, 0]
        elif check_num == 1:
            return [0, 0, 1]
        else:
            print('error')
    else:
        count_m1 = 0
        count_0 = 0
        count_p1 = 0
        
        diff_y = (yr[1]-yr[0])//3
        small_y = [(yr[0], yr[0]+diff_y), (yr[0]+diff_y, yr[0]+2*diff_y), (yr[0]+2*diff_y, yr[1])]
        diff_x = (xr[1]-xr[0])//3
        small_x = [(xr[0], xr[0]+diff_x), (xr[0]+diff_x, xr[0]+2*diff_x), (xr[0]+2*diff_x, xr[1])]

        for sm_y in small_y:
            for sm_x in small_x:
                temp = check(sm_y, sm_x)
                count_m1 += temp[0]
                count_0 += temp[1]
                count_p1 += temp[2]
        
        return [count_m1, count_0, count_p1]
                    

answer = check(yr, xr)

for an in answer:
    print(an)
