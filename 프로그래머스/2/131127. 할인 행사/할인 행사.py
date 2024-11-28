def solution(want, number, discount):
    answer = 0
    dic = {}

    for i, w in enumerate(want):
        dic[w] = i
    
    for i in range(len(discount) - 9):
        temp = number[:]
        
        for j in range(i, i + 10):
            if discount[j] in dic:
                temp[dic[discount[j]]] -= 1
        
        if all(x == 0 for x in temp):
            answer += 1
    
    return answer