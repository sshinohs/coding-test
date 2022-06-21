number_of_class = int(input())

score_str = input().split()

score_int = []

for ii in range(number_of_class):
    score_int.append(int(score_str[ii]))

score_max = max(score_int)

sum = 0
for ii in range(number_of_class):
    sum = sum + score_int[ii]/score_max*100

print(sum/number_of_class)