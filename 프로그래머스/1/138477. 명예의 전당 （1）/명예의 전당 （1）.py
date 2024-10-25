def solution(k, score):
    hall = []
    answer = []
    
    for i in range(len(score)):
        if len(hall) < k:
            hall.append(score[i])
            hall.sort()
            answer.append(hall[0])
        else:
            hall.sort() # 10 20 100
            if hall[0] >= score[i]: 
                answer.append(hall[0])
            else: 
                for j in range(len(hall)-1, -1, -1): 
                    if hall[j] <= score[i]: # 들어온 값이 원래 있던 값들보다 클 때
                        hall.insert(j+1, score[i])
                        hall.pop(0)
                        answer.append(hall[0])
                        break
    return answer