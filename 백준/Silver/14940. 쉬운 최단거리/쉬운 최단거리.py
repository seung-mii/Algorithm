from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
goal_x, goal_y = 0, 0

for i in range(n):
  line = list(map(int, input().split()))
  for j in range(m):
    graph[i][j] = line[j]

    if line[j] == 0:
      visited[i][j] = -1
    if line[j] == 2:
      goal_x, goal_y = i, j

def bfs(x, y):
  q = deque([(x, y)])
  visited[x][y] = 0

  while q:
    x, y = q.popleft()

    for i in range(4):
      dx = x + d[i][0]
      dy = y + d[i][1]

      if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] == 0:
        q.append((dx, dy))
        visited[dx][dy] = visited[x][y] + 1

bfs(goal_x, goal_y)

for i in range(n):
  for j in range(m):
    if visited[i][j] == -1:
      print(0, end=' ')
    elif i == goal_x and j == goal_y:
      print(0, end=' ')
    elif visited[i][j] == 0 and graph[i][j] == 1:
      print(-1, end=' ')
    else:
      print(visited[i][j], end=' ')
  print()