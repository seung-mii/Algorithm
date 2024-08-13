from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]
visited = [300001] * (n+1)
cities = []

for i in range(1, m+1):
  a, b = map(int, input().split())
  graph[a].append(b)

def bfs(x):
  q = deque([x])
  visited[x] = 0
  cities = []

  while q:
    node = q.popleft()

    for neighbor in graph[node] :
      if visited[neighbor] == 300001:
        q.append(neighbor)
        visited[neighbor] = visited[node]+1

    if visited[node] == k: 
      cities.append(node)

  if len(cities) == 0:
    cities.append(-1)
  return cities

cities = bfs(x)
cities.sort()
for city in cities:
  print(city)