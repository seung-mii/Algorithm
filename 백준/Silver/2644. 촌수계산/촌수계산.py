from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1) 

for _ in range(int(input())):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def bfs(v):
  q = deque([v]) 
  visited[v] = 1 
    
  while q:
    node = q.popleft()

    for neighbor in graph[node]:
      if visited[neighbor] == 0:
        visited[neighbor] = visited[node] + 1
        q.append(neighbor)

bfs(a)
if visited[b] != 0:
  print(visited[b] - 1)  # -1로 정확한 촌수 출력
else:
  print(-1)