while(True):
    try:
        data = input()
        nums = data.split()
        a = int(nums[0])
        b = int(nums[1])
        print(a+b)
    except:
        break