def solution(clothes):
    from collections import defaultdict

    dic = defaultdict(int)
    
    for c in clothes:
        dic[c[1]] += 1
    
    answer = 1
    for count in dic.values():
        print(count)
        answer *= (count + 1)  
    
    return answer - 1