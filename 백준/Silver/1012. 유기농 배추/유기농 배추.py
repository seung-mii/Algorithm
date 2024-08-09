for _ in range(int(input())):
  m, n, k = map(int, input().split())

  d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  graph = [[0] * (n) for _ in range(m)]
  visited = [[0] * (n) for _ in range(m)]
  cnt = 0

  for __ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1
    visited[x][y] = -1
    
  def dfs(x, y):
    stack = [(x, y)]
    visited[x][y] = 1

    while stack:
      x, y = stack.pop()

      for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]

        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1 and visited[nx][ny] == -1:
          stack.append((nx, ny))
          visited[nx][ny] = 1
  
  for x in range(m):
    for y in range(n):
      if visited[x][y] == -1:
        cnt += 1
        dfs(x, y)

  print(cnt)