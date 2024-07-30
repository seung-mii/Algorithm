import sys
input = sys.stdin.readline

n, k = map(int, input().split())
kettles = [int(input()) for _ in range(n)]

start, end = 0, max(kettles)
while start <= end:
  volume = 0
  mid = (start+end) // 2

  if mid == 0:  
    break
  
  for kettle in kettles:
    volume += (kettle // mid)

  if volume < k:
    end = mid - 1
  else:
    start = mid + 1

print(end)