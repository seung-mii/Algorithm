from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
start_x, start_y = 0, 0
people = 0

for i in range(n):
  s = input()
  for j in range(m):
    if s[j] == 'X':
      visited[i][j] = -1
    elif s[j] == 'I':
      start_x, start_y = i, j
    elif s[j] == 'P':
      graph[i][j] = 2

def bfs(x, y):
  cnt = 0
  q = deque([(x, y)])
  visited[x][y] = 1
  
  while q:
    x, y = q.popleft()

    for i in range(4):
      dx = x + d[i][0]
      dy = y + d[i][1]

      if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] == 0: 
        if graph[dx][dy] == 2:
          cnt += 1
        visited[dx][dy] = 1
        q.append([dx, dy])
  
  return cnt

people = bfs(start_x, start_y)
print('TT' if people == 0 else people)