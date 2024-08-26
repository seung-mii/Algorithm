from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(m)]
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(x, y):
  q = deque([(x, y)])
  graph[x][y] = 2
  
  while q:
    x, y = q.popleft() 

    for i in range(4):
      dx = x + d[i][0]
      dy = y + d[i][1]

      if 0 <= dx < m and 0 <= dy < n and graph[dx][dy] == 0:
        graph[dx][dy] = 2
        q.append([dx, dy])
        
for j in range(n):
  if graph[0][j] == 0:
    bfs(0, j)

print("YES" if 2 in graph[-1] else "NO")