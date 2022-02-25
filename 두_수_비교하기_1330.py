data = input()
nums = data.split()
a = int(nums[0])
b = int(nums[1])

if a>b:
    print(">")
elif a<b:
    print("<")
elif a==b:
    print("==")
