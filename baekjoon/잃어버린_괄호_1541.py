# import sys
# import math
# from itertools import permutations

# input = sys.stdin.readline

# data = input()[:-1]


# numerics = []
# operators = []
# buffer = ''
# for cha in data:
#     if cha == '+' or cha == '-':
#         if len(buffer) > 0:
#             numerics.append(int(buffer))
#             buffer = ''
#         operators.append(cha)
#     else:
#         buffer += cha
# numerics.append(int(buffer))

# min_val = math.inf

# for oper_order in permutations(list(range(len(operators))), len(operators)):
#     cal_result = numerics[oper_order[0] + 1]
#     for i in oper_order:
#         if operators[i] == '+':
#             cal_result += numerics[i]
#         elif operators[i] == '-':
#             cal_result -= oper
#         else:
#             print('error')

import sys

input = sys.stdin.readline

data = input()[:-1].split('-')

output = sum(map(int, data[0].split('+')))

for dat in data[1:]:
    sum_dat = sum(map(int, dat.split('+')))
    output -= sum_dat

print(output)



