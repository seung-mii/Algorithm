from collections import deque

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
size = []

for i in range(k):
  r, c = map(int, input().split())
  graph[r-1][c-1] = 1
  visited[r-1][c-1] = 1

def bfs(x, y):
  q = deque([(x, y)])
  visited[x][y] = 2
  size = 0

  while q:
    x, y = q.popleft()
    size += 1

    for i in range(4):
      dx = x + d[i][0]
      dy = y + d[i][1]

      if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] == 1 and graph[dx][dy] == 1:
        q.append((dx, dy))
        visited[dx][dy] = 2

  return size

for i in range(n):
  for j in range(m):
    if visited[i][j] == 1:
      size.append(bfs(i, j))

print(max(size))