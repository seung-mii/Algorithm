n = int(input())

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [[0] * (n+1) for _ in range(n+1)]
cnt = 0
res = []

for i in range(1, n+1):
  s = input()
  for j in range(1, n+1):
    graph[i][j] = int(s[j-1])

    if int(s[j-1]) == 1:
      visited[i][j] = -1
  
def dfs(x, y, num):
  visited[x][y] = num

  for i in range(4):
    nx = x + d[i][0]
    ny = y + d[i][1]

    if 0 < nx <= n and 0 < ny <= n and graph[nx][ny] == 1 and visited[nx][ny] == -1: 
      dfs(nx, ny, num) 

for x in range(1, n+1):
  for y in range(1, n+1):
    if visited[x][y] == -1:
      cnt += 1
      dfs(x, y, cnt)

for i in range(1, cnt+1):
  res.append(sum(row.count(i) for row in visited))
res.sort()

print(cnt)
for i in range(len(res)):
  print(res[i])