from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v) 
  graph[v].append(u) 

def bfs(v):
  order = 1
  q = deque([v])
  visited[v] = order
  
  while q:
    node = q.popleft() 
    graph[node].sort(reverse=True)

    for neighbor in graph[node]:
      if visited[neighbor] == 0:
        order += 1 
        visited[neighbor] = order
        q.append(neighbor)

bfs(r)
for i in range(1, n+1):
  print(visited[i])