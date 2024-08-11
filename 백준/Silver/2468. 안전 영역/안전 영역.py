import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
 
n = int(input())
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
graph = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]
max_n = 0

for i in range(n):
  num = list(map(int, input().split()))
  for j in range(n):
    graph[i][j] = num[j]
    if num[j] > max_n:
      max_n = num[j]
 
def dfs(x, y, water):
  visited[x][y] = 1

  for i in range(4):
    dx = x + d[i][0]
    dy = y + d[i][1]

    if 0 <= dx < n and 0 <= dy < n and visited[dx][dy] == 0 and graph[dx][dy] > water:
      dfs(dx, dy, water)

area = 0  
for water in range(0, max_n+1):
  visited = [[0] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if graph[i][j] <= water:
        visited[i][j] = -1 # 방문하면 안되는 지역
  
  pre_area = 0
  for i in range(n):
    for j in range(n):
      if visited[i][j] == 0:
        dfs(i, j, water)
        pre_area += 1

  area = max(area, pre_area)

print(area)