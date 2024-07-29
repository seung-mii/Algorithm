import sys
input = sys.stdin.readline

n,m = map(int, input().split())
amount = [int(input()) for i in range(n)]

start, end = max(amount), sum(amount)
while start <= end:
  mid = (start+end) // 2
  cnt = 1
  changes = mid

  for i in amount: 
    if changes - i < 0:
      cnt += 1
      changes = mid
    changes -= i 

  if cnt <= m:
    end = mid - 1
  else:
    start = mid + 1

print(mid)