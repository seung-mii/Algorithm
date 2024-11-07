def solution(n, words):
    index = -1
    dup = []
    
    for i in range(len(words)-1):
        cnt, net = words[i], words[i+1]
        
        # 끝말 안잇기
        if cnt[-1] != net[0]:
            index = i+1
            break
        
        # 중복
        if words.count(cnt) > 1:
            if cnt not in dup:
                dup.append(cnt)
            else:
                index = i
                break
        if words.count(net) > 1:
            if net not in dup:
                dup.append(cnt)
            else:
                index = i+1
                break
            
    answer = [(index % n) + 1, (index // n) + 1] if index != -1 else [0, 0]
    return answer