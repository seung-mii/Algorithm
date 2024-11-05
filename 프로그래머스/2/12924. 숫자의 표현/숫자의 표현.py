import math

def solution(n):
    answer = 1
    ary = []
    
    for i in range(1, math.ceil(n // 2)+2):
        ary.append(i)
        
    for i in range(len(ary)):
        temp = n - ary[i]
        for j in range(i+1, len(ary)):
            temp -= ary[j]
            
            if temp == 0:
                answer += 1
                break
            elif temp < 0:
                break
    
    return answer