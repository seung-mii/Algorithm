from collections import deque

def solution(maps):
    h, w = len(maps), len(maps[0])
    visited = [[0] * w for _ in range(h)]
    d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    
    def bfs(x, y):
        q = deque([(x, y, 1)])
        
        while q:
            x, y, dist = q.popleft()
            visited[x][y] = 1

            if x == h - 1 and y == w - 1:
                return dist
          
            for i in range(4):
                dx = x + d[i][0]
                dy = y + d[i][1]

                if 0 <= dx < h and 0 <= dy < w and visited[dx][dy] == 0 and maps[dx][dy] == 1:
                    q.append((dx, dy, dist + 1))
                    visited[dx][dy] = 1
        
        return -1
    return bfs(0, 0)