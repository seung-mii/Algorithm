from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
computer = []

for _ in range(m):
  a, b = map(int, input().split())
  graph[b].append(a)

def bfs(x):
  q = deque([x])
  cnt = 0

  visited = [False] * (n+1)
  visited[x] = True

  while q:
    node = q.popleft()

    for neighbor in graph[node]:
      if not visited[neighbor]:
        visited[neighbor] = True
        q.append(neighbor)
        cnt += 1

  return cnt

for i in range(1, n+1):
  computer.append(bfs(i))

for i in range(len(computer)):
  if computer[i] == max(computer):
    print(i+1, end=' ')