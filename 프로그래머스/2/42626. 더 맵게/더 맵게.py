import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while len(scoville) > 1 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        result = first + second * 2
        heapq.heappush(scoville, result)
        answer += 1
    
    if scoville[0] < K:
        return -1
    else:
        return answer