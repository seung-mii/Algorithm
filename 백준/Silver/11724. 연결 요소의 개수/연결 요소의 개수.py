import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for _ in range(m):
  u, v = map(int, input().split())
  graph[u][v] = 1
  graph[v][u] = 1

def dfs(v):
  stack = [v]
  visited[v] = 1

  while stack:
    node = stack.pop()

    for i in range(1, n+1):
      if visited[i] == 0 and graph[node][i] == 1:
        stack.append(i)
        visited[i] = 1

for i in range(1, n+1):
  if visited[i] == 0:
    cnt += 1
    dfs(i)

print(cnt)