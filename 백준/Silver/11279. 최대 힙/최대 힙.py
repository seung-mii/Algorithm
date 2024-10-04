import heapq
import sys
input = sys.stdin.readline

max_heap = []

for _ in range(int(input())):
  x = int(input())

  if x == 0:
    if len(max_heap) == 0:
      print(0)
    else:
      print(-heapq.heappop(max_heap))
  else:
    heapq.heappush(max_heap, -x)