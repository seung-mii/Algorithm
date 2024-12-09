from collections import Counter

def solution(topping):
    answer = 0
    type_count = Counter(topping)
    left = set()
    
    for t in topping:
        left.add(t)
        type_count[t] -= 1
        
        if type_count[t] == 0:
            del type_count[t]  
        
        if len(left) == len(type_count):
            answer += 1
    
    return answer