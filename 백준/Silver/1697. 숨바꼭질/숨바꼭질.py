from collections import deque

n, k = map(int, input().split())
graph = [0] * 100001

def bfs(v):
  q = deque([v])

  while q:
    v = q.popleft()

    if v == k:
      return graph[v]

    for next_v in (v-1, v+1, 2*v):
      if 0 <= next_v < 100001 and not graph[next_v]:
        graph[next_v] = graph[v] + 1
        q.append(next_v)

print(bfs(n))