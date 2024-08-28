import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
order = 1

for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

def dfs(v):
  global order
  visited[v] = order
  graph[v].sort()

  for neighbor in graph[v]:
    if visited[neighbor] == 0:
      order += 1
      dfs(neighbor)
  
dfs(r)

for i in range(n):
  print(visited[i+1])