from collections import deque

a, b = map(int, input().split())
graph = {}

def bfs(v):
    q = deque([v])
    graph[v] = 0
    
    while q:
        node = q.popleft()

        if node == b:
            return graph[node] + 1 

        for next_node in (2*node, int(str(node)+'1')):
            if next_node <= b and next_node not in graph: 
                graph[next_node] = graph[node] + 1
                q.append(next_node)
  
    return -1 

print(bfs(a))
