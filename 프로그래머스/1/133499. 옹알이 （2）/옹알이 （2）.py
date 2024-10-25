def solution(babbling):
    languge = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    
    for b in babbling:
        if "ayaaya" in b or "yeye" in b or "woowoo" in b or "mama" in b:
            continue
            
        for l in languge:
            b = b.replace(l, '.')
        
        b = b.replace('.', '')
        if b == '':
            answer += 1
            
    return answer