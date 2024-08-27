from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

def bfs(a, b):
  q = deque([a])
  visited[a] = 0

  if a == b:
    return 0

  while q:
    node = q.popleft() 

    for neighbor in graph[node]:
      if visited[neighbor] == 0:
        visited[neighbor] = visited[node] + 1
        q.append(neighbor)

        if neighbor == b:
          return visited[neighbor]

  return -1

print(bfs(a, b))