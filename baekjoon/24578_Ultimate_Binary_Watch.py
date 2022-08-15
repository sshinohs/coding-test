import sys
input = sys.stdin.readline

def output_str(check):
    if check == '0':
        print('.', end='')
    elif check == '1':
        print('*', end='')

n = list(input().strip())

nums = list(map(int, n))

nums_string = []
for i in nums:
    nums_string.append(f'{str(bin(i)[2:]):0>4}')

for i in range(4):
    output_str(nums_string[0][i])
    print(' ', end='')
    output_str(nums_string[1][i])
    print(' ', end='')
    print(' ', end='')
    print(' ', end='')
    output_str(nums_string[2][i])
    print(' ', end='')
    output_str(nums_string[3][i])
    print()

