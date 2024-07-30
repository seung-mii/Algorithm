import sys
input = sys.stdin.readline

s, c = map(int, input().split())
l = [int(input()) for i in range(s)]
remain = 0
best_remain = 0
start, end = 1, max(l)
while start <= end:
  mid = (start + end) // 2
  num = 0
  remain = 0

  for length in l:
    num += (length // mid)
    remain += (length % mid)

  if num > c:
    remain += (num - c) * mid
    best_remain = remain 
    start = mid + 1
  elif num == c:
    best_remain = remain 
    start = mid + 1
  else:
    end = mid - 1

print(best_remain)