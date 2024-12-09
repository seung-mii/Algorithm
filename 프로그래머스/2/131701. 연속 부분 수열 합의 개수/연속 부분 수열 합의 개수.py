def solution(elements):
    answer = set()
    length = len(elements)
    
    for i in range(1, length+1): # 1 ~ 5
        for j in range(length):
            if j+i > length-1: # 4 이상
                answer.add(sum(elements[j:j+i]) + sum(elements[:(j+i) % length]))
            else:
                answer.add(sum(elements[j:j+i]))
    
    return len(answer)