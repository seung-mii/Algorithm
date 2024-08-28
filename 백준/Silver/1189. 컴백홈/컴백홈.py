import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

r, c, k = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)] 
visited = [[0] * c for _ in range(r)] 
d = [(1, 0), (0, 1), (0, -1), (-1, 0)] 
num = 0 

def dfs(x, y, dis):
  global num

  if x == 0 and y == c-1:
    if dis == k:
      num += 1
    return

  visited[x][y] = 1

  for i in range(4):
    dx = x + d[i][0]
    dy = y + d[i][1]
     
    if 0 <= dx < r and 0 <= dy < c and not visited[dx][dy] and graph[dx][dy] != 'T':
      dfs(dx, dy, dis + 1)
   
  visited[x][y] = 0

dfs(r - 1, 0, 1) 
print(num) 