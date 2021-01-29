import heapq

def solution(n, works):
    heap = [-work for work in works]
    heapq.heapify(heap)

    for i in range(n):
        t = heapq.heappop(heap)
        if t == 0:
            return 0
        heapq.heappush(heap, t+1)

    return sum([work * work for work in heap])