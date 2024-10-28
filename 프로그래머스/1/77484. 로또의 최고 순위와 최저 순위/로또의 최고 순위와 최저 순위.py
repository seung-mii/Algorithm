def solution(lottos, win_nums):
    answer = [7, 7]
    zero = lottos.count(0)
    
    for l in lottos:
        if l in win_nums:
            answer[0] -= 1
            answer[1] -= 1
            
    if answer[1] != 1:
        answer[0] = answer[1] - zero
        
    if answer[0] == 7:
        answer[0] = 6
    if answer[1] == 7:
        answer[1] = 6
        
    return answer