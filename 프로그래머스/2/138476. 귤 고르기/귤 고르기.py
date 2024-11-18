def solution(k, tangerine):
    answer = 0
    total = 0
    dic = {}
    
    for t in tangerine:
        dic[t] = dic.get(t, 0) + 1
    
    counts = sorted(dic.values(), reverse=True)
    
    for count in counts:
        total += count
        answer += 1
        if total >= k:
            break
    
    return answer