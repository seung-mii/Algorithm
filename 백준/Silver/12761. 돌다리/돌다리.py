from collections import deque
import sys
input = sys.stdin.readline

a, b, n, m = map(int, input().split())
graph = [0] * 100001
visited = [0] * 100001

def bfs(v):
  q = deque([v])
  visited[v] = 0

  while q:
    v = q.popleft() 

    for next_v in (v-1, v+1, v-a, v-b, v+a, v+b, v*a, v*b):
      if 0 < next_v < 100001 and visited[next_v] == 0:
        visited[next_v] = visited[v] + 1
        q.append(next_v)

bfs(n)
print(visited[m])