from collections import deque
import sys
input = sys.stdin.readline
 
n = int(input())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1) 

for i in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a) 
 
def bfs(v):
  q = deque([v]) 
    
  while q:
    node = q.popleft()
    
    for neighbor in graph[node]:
      if visited[neighbor] == 0:
        visited[neighbor] = node
        q.append(neighbor)
 
bfs(1)
answer = visited[2:]
for x in answer:
  print(x)