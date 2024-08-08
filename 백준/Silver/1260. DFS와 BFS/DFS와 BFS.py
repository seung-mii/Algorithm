from collections import deque

n, m, v = map(int, input().split())
g = [[False] * (n+1) for i in range(n+1)]

for i in range(m):
  x, y = map(int, input().split())
  g[x][y] = True
  g[y][x] = True

visit1 = [False] * (n+1)
visit2 = [False] * (n+1)

def dfs(v):
  visit1[v] = True
  print(v, end=' ')

  for i in range(1, n+1):
    if visit1[i] == False and g[v][i] == True:
      dfs(i)

def bfs(v):
  q = deque([v])
  visit2[v] = True

  while q:
    v = q.popleft()
    print(v, end=' ')

    for i in range(1, n+1):
      if visit2[i] == False and g[v][i] == True:
        q.append(i)
        visit2[i] = True

dfs(v)
print()
bfs(v)