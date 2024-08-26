from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
d = [(0, 1), (1, 0)]

for i in range(n):
  line = list(map(int, input().split()))
  for j in range(n):
    graph[i][j] = line[j]

def bfs(x, y):
  q = deque([(x, y)])
  visited[x][y] = True
  
  while q:
    x, y = q.popleft() 

    for i in range(2):
      dx = x + (d[i][0] * graph[x][y])
      dy = y + (d[i][1] * graph[x][y])

      if 0 <= dx < n and 0 <= dy < n and not visited[dx][dy]:
        if graph[dx][dy] == -1:
          return 1

        q.append([dx, dy])
        visited[x][y] = True
  return 0
        
print('HaruHaru' if bfs(0, 0) == 1 else 'Hing')