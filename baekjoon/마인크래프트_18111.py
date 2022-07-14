import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

def cost_calculator(floor):
    spare = B
    time_cost = 0
    for row in board:
        for cell in row:
            diff = floor - cell
            if diff < 0:
                time_cost += abs(diff) * 2
                spare += abs(diff)
            else:
                time_cost += diff
                spare -= diff
    
    return time_cost, spare

# result = []
best = cost_calculator(0)
best_floor = 0
for i in range(1, 257):
    
    # print(i)
    compare = cost_calculator(i)
    # print('i', i)
    # print(compare)
    # print()
    if best[1] < 0 and compare[1] >= 0:
        best = compare
        best_floor = i
    elif best[1] >= 0 and compare[1] >= 0:
        # print('ho2')
        if best[0] >= compare[0]:
            best = compare
            best_floor = i
        elif best[0] < compare[0]:
            # print('ho3')
            break
    
print(best[0], best_floor)
# print(best_floor)
# print(best)
    