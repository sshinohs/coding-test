import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    apartment = [[i for i in range(n+1)]]
    # print(apartment)

    for i in range(1, k+1):
        apt_floor = [0]
        for j in range(1, n+1):
            apt_floor.append(sum(apartment[i-1][1:j+1]))
        apartment.append(apt_floor)
    print(apartment[k][n])