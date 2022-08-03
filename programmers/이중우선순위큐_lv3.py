import heapq
def solution(operations):
    
    min_heap = []
    max_heap = []
    
    for oper in operations:
        oper = oper.split()
        if oper[0] == 'I':
            heapq.heappush(min_heap, int(oper[1]))
            heapq.heappush(max_heap, -int(oper[1]))
        else:
            if len(min_heap) == 0:
                continue
            elif oper[1] == '1':
                max_value = -heapq.heappop(max_heap)
                min_heap.remove(max_value)
            else:
                min_value = heapq.heappop(min_heap)
                max_heap.remove(-min_value)
    
    if len(min_heap) > 0:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    else:
        return [0, 0]
    return answer