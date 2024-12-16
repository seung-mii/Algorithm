def solution(s):
    s = s[2:-2].split("},{")
    s = [list(map(int, group.split(","))) for group in s]  
    s.sort(key=len)  
    
    answer = []
    for group in s:
        for num in group:
            if num not in answer:  
                answer.append(num)
    
    return answer