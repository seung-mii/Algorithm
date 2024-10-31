def solution(id_list, report, k):
    answer = [0] * len(id_list)
    id = {}
    stop = {}
    
    for i in id_list:
        id[i] = []
        stop[i] = 0
        
    for r in report:
        s, e = r.split(' ')
        
        if e not in id[s]:
            id[s].append(e)
            stop[e] += 1
    
    for st in stop:
        if stop[st] >= k: # 2 > 2
            for idx, i in enumerate(id): # 
                if st in id[i]:
                    answer[idx] += 1
                
    return answer