def solution(keymap, targets):
    answer = []
    
    for target in targets:
        num = 0
        for t in target:
            temp_num = 999
            for k in keymap:
                if t in k:
                    temp_num = min(temp_num, k.index(t) + 1)
            num += temp_num
            if temp_num == 999:
                num = -1
                break
        answer.append(num)
    return answer