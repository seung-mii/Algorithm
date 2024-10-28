def solution(s):
    answer = 0
    first = ''
    x = 0
    no_x = 0
    
    for c in s:
        if first == '':
            first = c
            
        if c == first:
            x += 1
        else:
            no_x += 1
        
        if x == no_x:
            answer += 1
            x = 0
            no_x = 0
            first = ''
            
    if x != 0:
        answer += 1
        
    return answer