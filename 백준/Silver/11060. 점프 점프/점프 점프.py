from collections import deque

n = int(input())
graph = list(map(int, input().split()))
visited = [-1] * n

def bfs(x):
  q = deque([x])
  visited[x] = 0
  
  while q:
    index = q.popleft()
    
    for i in range(1, graph[index] + 1):
      next_index = index + i
      
      if next_index >= n: 
        continue
      
      if visited[next_index] == -1: 
        visited[next_index] = visited[index] + 1 
        q.append(next_index)
  
  return visited[n-1]

result = bfs(0)
print(result if result != -1 else -1)