c = int(input())
n = int(input())

visited = [0] * (c+1)
graph = [[0] * (c+1) for _ in range(c+1)]

for i in range(n):
  x, y = map(int, input().split())
  graph[x][y] = 1
  graph[y][x] = 1
  
def dfs(v):
  visited[v] = 1

  for i in range(1, c+1):
    if visited[i] == 0 and graph[v][i] == 1:
      dfs(i)

dfs(1)
print(visited.count(1) - 1)