import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

graph = [list(map(int, input().split())) for _ in range(5)]
d = [(1, 0), (0, 1), (0, -1), (-1, 0)]
nums = set()  # 중복을 방지하기 위해 set 사용

def dfs(x, y, num):
  if len(num) == 6:
    nums.add(num)
    return

  for i in range(4):
    dx = x + d[i][0]
    dy = y + d[i][1]

    if 0 <= dx < 5 and 0 <= dy < 5:
      dfs(dx, dy, num + str(graph[dx][dy]))
  
for i in range(5):
  for j in range(5):
    dfs(i, j, str(graph[i][j]))

print(len(nums))