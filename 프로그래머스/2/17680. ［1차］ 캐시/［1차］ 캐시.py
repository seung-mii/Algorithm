def solution(cacheSize, cities):
    answer = 0
    dic = {}
    
    if cacheSize == 0:
        return len(cities) * 5  
    
    for city in cities:
        c = city.lower()
        if c not in dic:
            if len(dic) == cacheSize > 0:
                dic.pop(max(dic, key = dic.get))
            dic[c] = 0
            answer += 5
        else:
            dic[c] = 0
            answer += 1
        
        for d in dic:
            dic[d] += 1
    
    return answer