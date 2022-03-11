n, k = map(int, input().split())

values = []
for ii in range(n):
    value = int(input())
    if value <= k:
        values.append(value)

count = 0
change = k
idx_end = len(values)-1
idx_now = idx_end
while(change != 0):
    if change >= values[idx_now]:
        cval = change // values[idx_now]
        change = change % values[idx_now]
        count = count + cval
    elif idx_now ==0 :
        break
    else:
        idx_now = idx_now - 1

print(count)