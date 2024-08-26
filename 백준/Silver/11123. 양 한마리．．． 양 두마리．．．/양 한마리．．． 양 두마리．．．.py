from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  h, w = map(int, input().split())
  graph = [[0] * w for _ in range(h)]
  visited = [[0] * w for _ in range(h)]
  d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
  num = 0

  for i in range(h):
    s = input()
    for j in range(w):
      if s[j] == '#':   # 양
        graph[i][j] = 1

  def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
      x, y = q.popleft() 

      for i in range(4):
        dx = x + d[i][0]
        dy = y + d[i][1]

        if 0 <= dx < h and 0 <= dy < w and visited[dx][dy] == 0 and graph[dx][dy] == 1:
          visited[dx][dy] = 1
          q.append([dx, dy])

  for i in range(h):
    for j in range(w):
      if visited[i][j] == 0 and graph[i][j] == 1:
        bfs(i, j)
        num += 1

  print(num)