from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  m, n, k = map(int, input().split())
  d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
  graph = [[0] * n for _ in range(m)]
  visited = [[-1] * n for _ in range(m)]
  num = 0

  for __ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1   # 배추 1, 안배추 0
    visited[x][y] = 0 # 방문하면안됨 -1, 방문안함 0, 방문함 1

  def dfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
      x, y = q.popleft()

      for i in range(4):
        dx = x + d[i][0]
        dy = y + d[i][1]

        if 0 <= dx < m and 0 <= dy < n and visited[dx][dy] == 0 and graph[dx][dy] == 1:
          visited[dx][dy] = 1
          q.append((dx, dy))

  for i in range(m):
    for j in range(n):
      if visited[i][j] == 0 and graph[i][j] == 1:
        num += 1
        dfs(i, j)

  print(num)