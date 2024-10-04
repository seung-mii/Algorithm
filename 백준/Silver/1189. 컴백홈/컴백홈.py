import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

r, c, k = map(int, input().split())
graph = [[0] * c for _ in range(r)]  
visited = [[0] * c for _ in range(r)]  
d = [(1, 0), (0, 1), (0, -1), (-1, 0)]  
num = 0

for i in range(r):
  s = list(input().strip())  
  for j in range(c):
    if s[j] == 'T':  
      graph[i][j] = -1  


def dfs(x, y, dis):
  global num
  
  if x == 0 and y == c - 1:
    if dis == k:  
      num += 1
    return
    
  visited[x][y] = 1
  
  for i in range(4):
    dx = x + d[i][0]
    dy = y + d[i][1]

    if 0 <= dx < r and 0 <= dy < c and visited[dx][dy] == 0 and graph[dx][dy] != -1:
      dfs(dx, dy, dis + 1)

  visited[x][y] = 0  

dfs(r - 1, 0, 1)
print(num)