d = [1,3,2,5,4]
budget = 9
answer = 0
while True:
    mininum = 100001
    for i, cost in enumerate(d):
        if cost < minimum:
            minimum = cost
    if minimum > budget:
        break
    d.pop(i)
    answer += 1
    budget -= minimum

print(answer)