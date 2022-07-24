num = int(input())

count = 0

total = 1
while True:
    count += 1
    if num <= total:
        print(count)
        break
    
    total += count * 6