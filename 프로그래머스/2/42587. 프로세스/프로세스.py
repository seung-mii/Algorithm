def solution(priorities, location):
    cnt = 1
    dic = {}
    
    for i, p in enumerate(priorities):
        dic[i] = p

    while cnt != len(dic) - 1:
        for d in dic:
            if max(dic.values()) == dic[d]:
                if d == location:
                    return cnt
                else:
                    dic[d] = -1
                    cnt += 1
    return cnt