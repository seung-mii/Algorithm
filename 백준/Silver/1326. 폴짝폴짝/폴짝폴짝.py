from collections import deque

n = int(input())
graph = list(map(int, input().split()))
start, end = map(int, input().split())

start -= 1
end -= 1

def bfs(start, end, n, graph):
  visited = [-1] * n
  q = deque([start])
  visited[start] = 0

  while q:
    v = q.popleft()

    for next_v in range(v + graph[v], n, graph[v]):
      if visited[next_v] == -1:
        visited[next_v] = visited[v] + 1
        q.append(next_v)
        if next_v == end:
          return visited[next_v]

    for next_v in range(v - graph[v], -1, -graph[v]):
      if visited[next_v] == -1:
        visited[next_v] = visited[v] + 1
        q.append(next_v)
        if next_v == end:
          return visited[next_v]

  return -1

result = bfs(start, end, n, graph)
print(result)