def solution(dartResult):
    answer = 0
    score = []
    s = ''
    
    for d in dartResult:
        if (d == 'S'):
            score.append(int(s) ** 1)
            s = ''
        elif (d == 'D'):
            score.append(int(s) ** 2)
            s = ''
        elif (d == 'T'):
            score.append(int(s) ** 3)
            s = ''
        elif (d == '*'):
            if (len(score) == 1):
                score[0] *= 2
            else:
                score[-1] *= 2
                score[-2] *= 2
        elif (d == '#'):
            score[-1] *= -1
        else:
            s += d
            
    answer = sum(score)
    return answer