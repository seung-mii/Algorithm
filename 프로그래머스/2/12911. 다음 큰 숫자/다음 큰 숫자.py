def solution(n):
    answer = n
    num = answer
    
    while answer == n:
        num += 1
        
        if format(n, 'b').count('1') == format(num, 'b').count('1'):
            answer = num
    
    return answer