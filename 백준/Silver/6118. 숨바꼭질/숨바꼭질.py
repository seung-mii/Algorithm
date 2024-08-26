from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
d = 0

for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def bfs(v):
  q = deque([v])
  visited[v] = 0
  
  while q:
    node = q.popleft() 

    for neighbor in graph[node]:
      if visited[neighbor] == 0:
        visited[neighbor] = visited[node] + 1
        q.append(neighbor)
        
bfs(1)
visited[1] = 0
print(visited.index(max(visited)), max(visited), visited.count(max(visited)), sep=' ')