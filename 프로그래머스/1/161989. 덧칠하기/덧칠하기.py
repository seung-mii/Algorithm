def solution(n, m, section):
    wall = [1] * n
    answer = 0
    
    for s in section:
        wall[s-1] = 0
    
    for i in range(len(wall)):
        if wall[i] == 0:
            answer += 1
            if i + (m-1) <= len(wall) - 1:
                wall[i:i+m] = [1] * m
            else:
                wall[i:len(wall)] = [1] * (len(wall) - i)
    return answer