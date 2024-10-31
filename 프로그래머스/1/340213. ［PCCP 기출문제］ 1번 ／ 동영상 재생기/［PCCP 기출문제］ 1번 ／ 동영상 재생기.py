def opening(total):
    start = (total[2][0] * 60) + total[2][1]
    end = (total[3][0] * 60) + total[3][1]
    cur = (total[1][0] * 60) + total[1][1]
    
    if start <= cur < end:
        total[1] = [total[3][0], total[3][1]]
    
    return total

def solution(video_len, pos, op_start, op_end, commands):
    total = [
        list(map(int, video_len.split(":"))),
        list(map(int, pos.split(":"))),
        list(map(int, op_start.split(":"))),
        list(map(int, op_end.split(":")))
    ]
    
    # 오프닝 구간 확인
    opening(total)
        
    # commands 처리
    for c in commands:
        if c == "next":
            total[1][1] += 10
        else:
            total[1][1] -= 10
        
        # 초 단위 조정: 60초 이상
        if total[1][1] >= 60:
            total[1][0] += total[1][1] // 60
            total[1][1] %= 60
        # 초 단위 조정: 0초 이하
        elif total[1][1] < 0:
            total[1][0] -= 1
            total[1][1] += 60 

        # 0:0 이하
        if total[1][0] < 0 or (total[1][0] == 0 and total[1][1] < 0):
            total[1] = [0, 0] 
        
        # video_len 초과
        if total[1][0] > total[0][0] or (total[1][0] == total[0][0] and total[1][1] > total[0][1]):
            total[1] = [total[0][0], total[0][1]]
        
        opening(total)
    
    m = '0' + str(total[1][0]) if 0 <= total[1][0] < 10 else str(total[1][0])
    s = '0' + str(total[1][1]) if 0 <= total[1][1] < 10 else str(total[1][1])
    return m + ':' + s
