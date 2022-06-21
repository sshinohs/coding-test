data = input()
num_origin = int(data)

num_loop = num_origin

num_next = -1

iter = 0

while(num_origin != num_next):
    iter = iter+1

    num_check = (num_loop//10) + (num_loop%10)

    num_next = (num_loop%10)*10 + (num_check%10)

    num_loop = num_next

print(iter)