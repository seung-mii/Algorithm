def solution(board, h, w):
    color = board[h][w]
    d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    answer = 0
    
    for i in range(4):
        if 0 <= h + d[i][0] < len(board) and 0 <= w + d[i][1] < len(board[0]):
            if board[h + d[i][0]][w + d[i][1]] == color:
                answer += 1 
    
    return answer