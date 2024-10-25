def solution(babbling):
    languge = ['aya', 'ye', 'woo', 'ma']
    no = ['ayaaya', 'yeye', 'woowoo', 'mama']
    answer = 0
    
    for b in babbling:
        if any(babbling in b for babbling in no): 
            continue
            
        for l in languge:
            b = b.replace(l, '.')
        
        b = b.replace('.', '')
        if b == '':
            answer += 1
            
    return answer