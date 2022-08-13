import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

count = 0
for i in range(N,0,-1):
     a = r//2**(i-1)
     b = c//2**(i-1)
     count += (a*2+b)*2**(2*(i-1))
     r = r%2**(i-1)
     c = c%2**(i-1)
    #  print(i, a, b, count)

print(count)