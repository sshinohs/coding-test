import sys
# import heapq

num_cases = int(sys.stdin.readline())

for _ in range(num_cases):
    sums_chapter = []
    num_chapter = int(sys.stdin.readline())
    sizes_chapter = list(map(int, sys.stdin.readline().split()))
    count = 0

    for i in range(num_chapter-1):
        sums_chapter.append(sizes_chapter[i]+sizes_chapter[i+1])
    
    while len(sizes_chapter) > 1:

        temp = min(sums_chapter)
        index = sums_chapter.index(temp)

        count += temp
        
        sizes_chapter.pop(index)
        sizes_chapter.pop(index)
        sizes_chapter.insert(index, temp)

        sums_chapter.pop(index)
        
        if index < len(sizes_chapter)-1:
            sums_chapter.pop(index)
            sums_chapter.insert(index, sizes_chapter[index] + sizes_chapter[index+1])
        if index > 0:
            sums_chapter.pop(index-1)
            sums_chapter.insert(index-1, sizes_chapter[index-1] + sizes_chapter[index])
    
    print(count)