loop_num = int(input())

for ii in range(1, loop_num+1):
    data = input()
    nums = data.split()
    a = int(nums[0])
    b = int(nums[1])
    print("Case #"+str(ii)+": "+str(a+b))