from collections import deque
import sys
input = sys.stdin.readline

a, k = map(int, input().split())
graph = [0] * (k + 1)

def bfs(v):
  q = deque([v])
  graph[v] = 0

  while q:
    v = q.popleft()

    if v == k:
      break

    for next_v in (v+1, 2*v):
      if next_v <= k and graph[next_v] == 0:
        graph[next_v] = graph[v] + 1
        q.append(next_v)

bfs(a)
print(graph[k])