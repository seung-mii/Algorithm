def solution(s):
    zero = 0
    cnt = 0
    
    while s != '1':
        zero += s.count('0')
        cnt += 1
        s = s.replace('0', '')
        s = format(len(s), 'b')
    
    return [cnt, zero]