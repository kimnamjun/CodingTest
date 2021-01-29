import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    answer = 0
    while len(scoville) >= 2:
        answer += 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        c = a + b * 2
        heapq.heappush(scoville, c)
        if scoville[0] >= K:
            return answer
    
    return -1