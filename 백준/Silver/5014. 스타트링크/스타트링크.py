from collections import deque

f, s, g, u, d = map(int, input().split())
graph = [0] * (f+1)

def bfs(v):
  q = deque([v])
  graph[v] = 1
  
  while q:
    node = q.popleft()

    if node == g:
      return graph[g] - 1

    for next_node in (node+u, node-d):
      if 0 < next_node <= f and graph[next_node] == 0:
        q.append(next_node)
        graph[next_node] = graph[node] + 1

  return 'use the stairs'   

print(bfs(s))