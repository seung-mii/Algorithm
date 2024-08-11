import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

while True:
  w, h = map(int, input().split())
  d = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
  graph = [[0] * w for _ in range(h)]
  visited = [[0] * w for _ in range(h)]

  if w == 0 and h == 0:
    break

  for i in range(h):
    num = list(map(int, input().split()))
    for j in range(w):
      graph[i][j] = num[j]
      if num[j] == 0:
        visited[i][j] = -1
  
  def dfs(x, y):
    visited[x][y] = 1

    for i in range(8):
      dx = x + d[i][0]
      dy = y + d[i][1]

      if 0 <= dx < h and 0 <= dy < w and visited[dx][dy] == 0 and graph[dx][dy] == 1:
        dfs(dx, dy)

  area = 0
  for i in range(h):
    for j in range(w):
      if visited[i][j] == 0:
        dfs(i, j)
        area += 1

  print(area)