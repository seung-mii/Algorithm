import sys
input = sys.stdin.readline

m,n = map(int, input().split())
snacks = list(map(int, input().split()))
length = 0

start, end = 1, max(snacks)
while start <= end:
  mid = (start+end) // 2
  get = 0

  for snack in snacks: 
    get += snack // mid

  if get >= m:
    length = max(length, mid)
    start = mid + 1
  else:
    end = mid - 1

print(length)