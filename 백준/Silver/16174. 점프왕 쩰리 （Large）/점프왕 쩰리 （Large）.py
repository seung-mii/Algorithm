from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
d = [(0, 1), (1, 0)]

def bfs(x, y):
  q = deque([(x, y)])

  while q:
    x, y = q.popleft()

    if graph[x][y] == 0:
      continue

    save = graph[x][y]
    graph[x][y] = 0 

    for i in range(2):
      dx = x + d[i][0] * save
      dy = y + d[i][1] * save

      if 0 <= dx < n and 0 <= dy < n:
        if graph[dx][dy] == -1:
          return True
        q.append([dx, dy])

  return False

print('HaruHaru' if bfs(0, 0) else 'Hing')