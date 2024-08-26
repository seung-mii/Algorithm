from collections import deque

m, n = map(int, input().split())
graph = [[0] * n for _ in range(m)]
visited = [[0] * n for _ in range(m)]
d = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
cnt = 0 

for i in range(m):
  line = list(map(int, input().split()))
  for j in range(n):
    graph[i][j] = line[j]

    if line[j] == 0:
      visited[i][j] = -1

def bfs(x, y):
  q = deque([(x, y)])
  visited[x][y] = 1
  
  while q:
    x, y = q.popleft() 

    for i in range(8):
      dx = x + d[i][0]
      dy = y + d[i][1]

      if 0 <= dx < m and 0 <= dy < n and visited[dx][dy] == 0:
        visited[dx][dy] = 1
        q.append([dx, dy])
        
for i in range(m):
  for j in range(n):
    if visited[i][j] == 0:
      bfs(i, j)
      cnt += 1

print(cnt)