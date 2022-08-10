import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

nums = []
while True:
    try:
        nums.append(int(input()))
    except:
        break

def postorder(nums, st, ed):
    if st < ed:
        a = nums[st]        
        count = st + 1
        b_st = count
        while count < ed:
            if nums[count] >= a:
                b_ed = count
                break
            count += 1
        else:
            b_ed = ed
        
        c_st = count
        while count < ed:
            c_ed = count
            count += 1
        else:
            c_ed = ed
        
        postorder(nums, b_st, b_ed)
        postorder(nums, c_st, c_ed)
        print(a)

postorder(nums, 0, len(nums))