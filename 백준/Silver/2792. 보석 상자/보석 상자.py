import sys
input = sys.stdin.readline

n, m = map(int, input().split())
colors = [int(input()) for _ in range(m)]

start, end = 1, max(colors)
result = end
while start <= end:
  mid = (start + end) // 2
  cnt = 0

  for color in colors:
    if color <= mid:
      cnt += 1
      continue
    
    if color % mid == 0:
      cnt += color // mid
    else:
      cnt += color // mid + 1

  if cnt > n: 
    start = mid + 1
  else:
    end = mid - 1
    result = min(result, mid)

print(result)