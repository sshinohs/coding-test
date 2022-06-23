import sys
import math

T = int(sys.stdin.readline())

for _ in range(T):
    K = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))

    dp = [[0] * K]

    sums = [0]

    for i in range(0, K):
        sums.append(sums[-1] + data[i])

    # print(sums)
    # print(dp)

    for i in range(1, K):
        dp_row = []
        for j in range(K-i):
            dp_temp = math.inf
            for k in range(i):
                dp_temp = min(dp_temp, dp[k][j] + dp[i-k-1][j+k+1] + sums[j+i+1] - sums[j])
            dp_row.append(dp_temp)
        dp.append(dp_row)
    
    # print(dp)
    print(dp[K-1][0])
    
    
    # for i in range()



# import sys
# # import heapq

# num_cases = int(sys.stdin.readline())

# for _ in range(num_cases):
#     sums_chapter = []
#     num_chapter = int(sys.stdin.readline())
#     sizes_chapter = list(map(int, sys.stdin.readline().split()))
#     count = 0

#     for i in range(num_chapter-1):
#         sums_chapter.append(sizes_chapter[i]+sizes_chapter[i+1])
    
#     while len(sizes_chapter) > 1:

#         temp = min(sums_chapter)
#         index = sums_chapter.index(temp)

#         count += temp
        
#         sizes_chapter.pop(index)
#         sizes_chapter.pop(index)
#         sizes_chapter.insert(index, temp)

#         sums_chapter.pop(index)
        
#         if index < len(sizes_chapter)-1:
#             sums_chapter.pop(index)
#             sums_chapter.insert(index, sizes_chapter[index] + sizes_chapter[index+1])
#         if index > 0:
#             sums_chapter.pop(index-1)
#             sums_chapter.insert(index-1, sizes_chapter[index-1] + sizes_chapter[index])
    
#     print(count)