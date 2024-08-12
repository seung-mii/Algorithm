from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
cnt = []

for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def bfs(v):
  q = deque([v])
  visited[v] = 1
  
  while q:
    node = q.popleft()

    for neighbor in graph[node]:
      if visited[neighbor] == 0:
        visited[neighbor] = visited[node] + 1
        q.append(neighbor)

for i in range(1, n+1):
  visited = [0] * (n+1)
  bfs(i)
  cnt.append(sum(visited))

print(cnt.index(min(cnt)) + 1)