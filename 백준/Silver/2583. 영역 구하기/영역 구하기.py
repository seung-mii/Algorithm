import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
graph = [[0] * n for __ in range(m)]
visited = [[0] * n for __ in range(m)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
areas = []
cnt = 0

for _ in range(k):
  l_x, l_y, r_x, r_y = map(int, input().split())
  for i in range(l_x, r_x):
    for j in range(l_y, r_y):
      graph[j][i] = -1
      visited[j][i] = -1

def dfs(x, y):
  stack = [(x, y)]
  area_size = 0

  while stack:
    x, y = stack.pop()

    if visited[x][y] == 0:
      visited[x][y] = 1
      area_size += 1

      for i in range(4):
        dx = x + d[i][0]
        dy = y + d[i][1]

        if 0 <= dx < m and 0 <= dy < n and visited[dx][dy] == 0:
          stack.append((dx, dy))

  return area_size

for i in range(m):
  for j in range(n):
    if visited[i][j] == 0:
      cnt += 1
      areas.append(dfs(i, j)) 

areas.sort()
print(cnt)
print(" ".join(map(str, areas)))