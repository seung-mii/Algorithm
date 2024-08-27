from collections import deque

n = int(input())
graph = [[] * 28 for _ in range(28)]

for _ in range(n):
  u, v = map(str, input().split(' is '))
  u = ord(u) - 97
  v = ord(v) - 97
  graph[u].append(v)


def bfs(u, v):
  q = deque([u])
  visited = [0] * 28
  visited[u] = 1

  while q:
    node = q.popleft()

    if node == v:
      return 'T'

    for neighbor in graph[node]:
      if visited[neighbor] == 0:
        visited[neighbor] = visited[node] + 1
        q.append(neighbor)

  return 'F'

m = int(input())
for _ in range(m):
  u, v = map(str, input().split(' is '))
  u = ord(u) - 97
  v = ord(v) - 97

  print(bfs(u, v))