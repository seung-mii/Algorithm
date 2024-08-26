from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * (n) for _ in range(n)]
visited = [[0] * (n) for _ in range(n)] 
d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
start_x, start_y, end_x, end_y = map(int, input().split())

def bfs(x, y):
  q = deque([(x, y)])
  visited[x][y] = 0
  
  while q:
    x, y = q.popleft() 

    if x == end_x and y == end_y:
      break

    for i in range(6):
      dx = x + d[i][0]
      dy = y + d[i][1]

      if 0 <= dx < n and 0 <= dy < n and visited[dx][dy] == 0:
        visited[dx][dy] = visited[x][y] + 1
        q.append([dx, dy])
        
bfs(start_x, start_y)
print(-1 if visited[end_x][end_y] == 0 else visited[end_x][end_y])