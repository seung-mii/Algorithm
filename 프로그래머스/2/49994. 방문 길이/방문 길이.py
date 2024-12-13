def solution(dirs):
    answer = 0
    x, y = 5, 5
    visited = set()
    dic = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}

    for di in dirs:
        dx = x + dic[di][0]
        dy = y + dic[di][1]
        
        if 0 <= dx <= 10 and 0 <= dy <= 10:
            path = ((x, y), (dx, dy))
            reverse_path = ((dx, dy), (x, y))  
            
            if path not in visited:
                visited.add(path)
                visited.add(reverse_path)  
                answer += 1
                
            x, y = dx, dy
            
    return answer