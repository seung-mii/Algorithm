from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  l = int(input())
  visited = [[0] * l for __ in range(l)]
  d = [(-2, -1), (2, -1), (-2, 1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
  start_x, start_y = map(int, input().split())
  goal_x, goal_y = map(int, input().split())

  def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
      node_x, node_y = q.popleft()

      for i in range(8):
        dx = node_x + d[i][0]
        dy = node_y + d[i][1]

        if 0 <= dx < l and 0 <= dy < l and visited[dx][dy] == 0:
          visited[dx][dy] = visited[node_x][node_y] + 1
          q.append((dx, dy))
      
      if node_x == goal_x and node_y == goal_y:
        break

  bfs(start_x, start_y)
  print(visited[goal_x][goal_y] - 1)