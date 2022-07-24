# I refer to the following site
# https://jiwon-coding.tistory.com/21

n,m = list(map(int,input().split()))

s = []
global count
count = 0
def dfs():
    global count
    count = count+1
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()

print(count)