import sys


input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

board = []

for _ in range(N):
    board.append(list(' '*(N//3*6-1)))

def star_cutter(arr,st_i, st_j, n):
    if n//2 >= 6:
        star_cutter(arr, st_i, st_j + n//2, n//2)
        star_cutter(arr, st_i + n//2, st_j, n//2)
        star_cutter(arr, st_i + n//2, st_j + n, n//2)
    elif n//2 == 3:
        last_cutter(arr, st_i, st_j + n//2)
        last_cutter(arr, st_i + n//2, st_j)
        last_cutter(arr, st_i + n//2, st_j + n)

def last_cutter(arr, st_i, st_j):
        arr[st_i][st_j:st_j+5] = list('  *  ')
        arr[st_i+1][st_j:st_j+5] = list(' * * ')
        arr[st_i+2][st_j:st_j+5] = list('*****')


if N == 3:
    last_cutter(board, 0, 0)
else:
    star_cutter(board, 0, 0, N)

for row in board:
    for num in row:
        print(num)
    print('\n')