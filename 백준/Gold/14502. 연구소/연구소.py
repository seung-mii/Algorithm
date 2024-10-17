import sys
import copy
from collections import deque
from itertools import combinations

n, m = map(int, input().split()) 
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
graph = [list(map(int, input().split())) for _ in range(n)]
max_count = 0
empty = []
virus = []

for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      empty.append((i, j))
    elif graph[i][j] == 2:
      virus.append((i, j))

def bfs(temp_graph, temp_virus):
  q = deque(temp_virus)

  while q:
    x, y = q.popleft()
    
    for i in range(4):
      dx = x + d[i][0]
      dy = y + d[i][1]
      
      if 0 <= dx < n and 0 <= dy < m and temp_graph[dx][dy] == 0:
        temp_graph[dx][dy] = 2
        q.append((dx, dy))

def safe(temp_graph):
  count = sum(row.count(0) for row in temp_graph)
  return count
  
for walls in combinations(empty, 3):
  temp_graph = copy.deepcopy(graph)
  for x, y in walls:
    temp_graph[x][y] = 1

  bfs(temp_graph, virus)

  count = safe(temp_graph)
  max_count = max(count, max_count)

print(max_count)