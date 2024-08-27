from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))
visited = [0] * n
s = int(input()) - 1

def bfs(v):
  q = deque([v])
  visited[v] = 1

  while q:
    v = q.popleft()

    for next_v in (v - graph[v], v + graph[v]):
      if 0 <= next_v < n and visited[next_v] == 0:
        visited[next_v] = visited[v] + 1
        q.append(next_v)

bfs(s)
print(len(visited) - visited.count(0))