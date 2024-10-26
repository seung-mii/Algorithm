def solution(N, stages):
    answer = []
    fail = []
    
    stages.sort()
    for i in range(N):
        if len(stages) != 0:
            fail.append(stages.count(i+1)/len(stages))
            for _ in range(stages.count(i+1)):
                stages.pop(0)
        else:
            fail.append(0)
    
    for _ in range(N):
        answer.append(fail.index(max(fail)) + 1)
        max_index = fail.index(max(fail))
        fail[max_index] = -100
    
    return answer