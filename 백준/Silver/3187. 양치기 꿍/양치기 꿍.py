from collections import deque
import sys

r, c = map(int, input().split())
graph = [[0] * c for _ in range(r)]
visited = [[0] * c for _ in range(r)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
num = [0, 0]

for i in range(r):
  s = input()
  for j in range(c):
    if s[j] == 'k':   # 양
      graph[i][j] = 1
    elif s[j] == 'v': # 늑대
      graph[i][j] = 2
    elif s[j] == '#': # 울타리
      visited[i][j] = -1

def bfs(x, y):
  q = deque([(x, y)])
  visited[x][y] = 1
  cnt = [0, 0]

  if graph[x][y] == 1:
    cnt[0] += 1
  if graph[x][y] == 2:
    cnt[1] += 1

  while q:
    x, y = q.popleft() 

    for i in range(4):
      dx = x + d[i][0]
      dy = y + d[i][1]

      if 0 <= dx < r and 0 <= dy < c and visited[dx][dy] == 0: 
        if graph[dx][dy] == 1:
          cnt[0] += 1
        if graph[dx][dy] == 2:
          cnt[1] += 1
        visited[dx][dy] = 1
        q.append([dx, dy])

  return cnt

for i in range(r):
  for j in range(c):
    if visited[i][j] == 0:
      temp = bfs(i, j)
      if temp[0] > temp[1]:
        temp[1] = 0
      else: 
        temp[0] = 0
      num[0] += temp[0]
      num[1] += temp[1]

for i in range(2):
  print(num[i], end=' ')