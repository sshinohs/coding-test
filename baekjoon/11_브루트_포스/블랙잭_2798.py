meta_data = input().split()

card_number = int(meta_data[0])

criteria = int(meta_data[1])

card_value = input().split()

sums = []

for ii in range(card_number):
    first_card = int(card_value[ii])
    for jj in range(card_number):
        if ii==jj:
            continue
        else:
            second_card = int(card_value[jj])
        for kk in range(card_number):
            if ii==kk or jj==kk:
                continue
            else:
                third_card = int(card_value[kk])
                sums.append(first_card+second_card+third_card)

approx_value = 0

for sum_value in sums:
    if abs(approx_value-criteria) > abs(sum_value-criteria) and (sum_value-criteria) <= 0:
        approx_value = sum_value

print(approx_value)