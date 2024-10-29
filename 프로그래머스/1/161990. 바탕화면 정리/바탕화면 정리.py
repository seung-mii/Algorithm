def solution(wallpaper):
    answer = [50, 50, 0, 0]
    
    for idx, wall in enumerate(wallpaper):
        for i, w in enumerate(wall):
            if w == '#':
                answer[0] = min(answer[0], idx)
                answer[1] = min(answer[1], i)
                answer[2] = max(answer[2], idx + 1)
                answer[3] = max(answer[3], i + 1)
            
    return answer