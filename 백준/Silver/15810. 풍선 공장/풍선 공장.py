import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))

start, end = 1, max(a) * m
while start <= end:
  mid = (start+end) // 2
  balloon = 0
  
  for time in a:
    balloon += mid // time

  if balloon >= m:
    end = mid - 1
  else:
    start = mid + 1

print(start)