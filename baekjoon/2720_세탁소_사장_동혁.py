import sys

input = sys.stdin.readline

for _ in range(int(input())):
    change = int(input())
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0
    
    if change >= 25:
        quarter = change // 25
        change %= 25
    
    if change >= 10:
        dime = change // 10
        change %= 10
    
    if change >= 5:
        nickel = change // 5
        change %= 5
    
    penny = change

    print(quarter, dime, nickel, penny)
        