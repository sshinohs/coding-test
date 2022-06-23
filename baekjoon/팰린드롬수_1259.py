import sys
import math

input = sys.stdin.readline

while True:
    val = input()
    if int(val) == 0:
        break
    len_val = len(val)
    flag = True
    for i in range(math.ceil(len_val/2)):
        if  val[i] != val[-(i+2)]:
            flag = False
    
    if flag:
        print('yes')
    else:
        print('no')