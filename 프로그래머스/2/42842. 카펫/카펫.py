def solution(brown, yellow):
    total = brown + yellow
    
    for height in range(3, total // 2 + 1):
        width = total // height
            
        if width >= height:
            if (width - 2) * (height - 2) == yellow:
                return [width, height]