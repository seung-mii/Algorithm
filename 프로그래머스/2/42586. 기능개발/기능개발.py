import math

def solution(progresses, speeds):
    answer = []
    day = []
    
    for i, p in enumerate(progresses):
        day.append(math.ceil((100-p) / speeds[i]))
    print(day)
    
    temp = day[0]
    day.pop(0)
    cnt = 1
    for d in day:
        if d <= temp:
            cnt += 1
        else:
            answer.append(cnt)
            temp = d
            cnt = 1
    answer.append(cnt)
    
    return answer