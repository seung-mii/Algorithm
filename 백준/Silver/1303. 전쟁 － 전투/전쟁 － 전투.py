from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
total = [0, 0]

for i in range(n):
  s = input()
  for j in range(m):
    if s[j] == 'W': # 우리팀
      graph[i][j] = 1
    else:
      graph[i][j] = 2

def bfs(x, y):
  q = deque([(x, y)])
  visited[x][y] = 1
  cnt = 0
  team = graph[x][y]
  
  while q:
    x, y = q.popleft()

    for i in range(4):
      dx = x + d[i][0]
      dy = y + d[i][1]

      if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] == 0 and graph[dx][dy] == team: 
        cnt += 1
        visited[dx][dy] = 1
        q.append([dx, dy])
  
  return cnt + 1

for i in range(n):
  for j in range(m):
    if visited[i][j] == 0:
      if graph[i][j] == 1:
        total[0] += (bfs(i, j)**2)
      else:
        total[1] += (bfs(i, j)**2)

for i in range(2):
  print(total[i], end=' ')