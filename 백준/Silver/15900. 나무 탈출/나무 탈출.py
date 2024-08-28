import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
depth = [0] * (n+1)
ans = 0

for _ in range(n-1):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

def dfs(v):
  visited[v] = 1

  for neighbor in graph[v]:
    if visited[neighbor] == 0:
      depth[neighbor] = depth[v] + 1
      dfs(neighbor)
  
dfs(1)

for i in range(2, n+1):
  if len(graph[i]) == 1: 
    ans += depth[i]

print("No" if (ans % 2 == 0) else "Yes")