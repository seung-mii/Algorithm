from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (m) for _ in range(n)]
safety = [[0] * (m) for _ in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
shark = []

for i in range(n):
  line = list(map(int, input().split()))
  for j in range(m):
    graph[i][j] = line[j]

    if line[j] == 1:
      shark.append([i, j])

def bfs(x, y):
  q = deque([(x, y)])
  visited = [[0] * (m) for _ in range(n)] 
  visited[x][y] = 1
  safety[x][y] = 0
  
  while q:
    x, y = q.popleft() 

    for i in range(8):
      dx = x + d[i][0]
      dy = y + d[i][1]

      if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] == 0 and graph[dx][dy] == 0:
        if safety[dx][dy] != 0:
          safety[dx][dy] = min(safety[dx][dy], safety[x][y] + 1)
        else:
          safety[dx][dy] = safety[x][y] + 1
        visited[dx][dy] = 1
        q.append([dx, dy])

for i in range(len(shark)):
  x = shark[i][0]
  y = shark[i][1]
  bfs(x, y)

max = 0
for i in range(n):
  for j in range(m):
    if max < safety[i][j]:
      max = safety[i][j]

print(max)