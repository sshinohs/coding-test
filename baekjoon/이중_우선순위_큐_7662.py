import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    h_min = []
    h_max = []
    nums = {}
    k = int(input())
    for _ in range(k):
        command = input().split()
        val = int(command[1])
        if command[0] == 'I':
            heapq.heappush(h_min, val)
            heapq.heappush(h_max, -val)
            if val not in nums:
                nums[val] = 1
            else:
                nums[val] += 1
        elif command[0] == 'D':
            if val == 1:
                while h_max and nums[-h_max[0]] == 0:
                    heapq.heappop(h_max)
                if h_max:
                    nums[-h_max[0]] -= 1
                    heapq.heappop(h_max)
            elif val == -1:
                while h_min and nums[h_min[0]] == 0:
                    heapq.heappop(h_min)
                if h_min:
                    nums[h_min[0]] -= 1
                    heapq.heappop(h_min)
    while h_max and nums[-h_max[0]] == 0:
        heapq.heappop(h_max)        
    while h_min and nums[h_min[0]] == 0:
        heapq.heappop(h_min)
    if h_min:
        print(-heapq.heappop(h_max), heapq.heappop(h_min))
    else:
        print('EMPTY')