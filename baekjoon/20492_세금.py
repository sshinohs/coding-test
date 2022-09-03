import sys

input = sys.stdin.readline

prize = int(input())

print(round(prize*0.78), round(prize*(0.8+0.2*0.78)))