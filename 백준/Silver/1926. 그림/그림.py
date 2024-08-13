n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cnt = 0
areas = [0]

for i in range(n):
  num = list(map(int, input().split()))
  for j in range(m):
    graph[i][j] = num[j]

    if num[j] == 0:
      visited[i][j] = -1

def dfs(x, y):
  stack = [(x, y)]
  visited[x][y] = 1
  area = 1

  while stack:
    x, y = stack.pop()

    for i in range(4):
      dx = x + d[i][0]
      dy = y + d[i][1]

      if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] == 0:
        stack.append((dx, dy))
        visited[dx][dy] = 1
        area += 1

  return area

for i in range(n):
  for j in range(m):
    if visited[i][j] == 0:
      areas.append(dfs(i, j))
      cnt += 1

print(cnt)
print(max(areas))