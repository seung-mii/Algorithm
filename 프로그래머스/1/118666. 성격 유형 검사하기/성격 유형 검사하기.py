def solution(survey, choices):
    answer = ''
    ary = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    aryC = ['RT', 'TR', 'CF', 'FC', 'JM', 'MJ', 'AN', 'NA']
    category = {'R' : 0, 'T' : 0}, {'C' : 0, 'F' : 0}, {'J' : 0, 'M' : 0}, {'A' : 0, 'N' : 0}
    
    for i in range(len(survey)):
        s = survey[i]
        c = choices[i]
        
        if 0 < c < 4:
            category[int(aryC.index(s) // 2)][s[0]] += (4-c)
        else: 
            category[int(aryC.index(s) // 2)][s[1]] += (c-4)
    
    jump = 0
    for i, c in enumerate(category):
        jump += (i * 2)
        if category[i][ary[0+jump]] < category[i][ary[1+jump]]:
            answer += ary[1+jump]
        elif category[i][ary[0+jump]] > category[i][ary[1+jump]]:
            answer += ary[0+jump]
        else:
            answer += min(category[i])
        jump = 0
                
    return answer