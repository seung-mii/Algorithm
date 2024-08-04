import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [int(input()) for i in range(n)]
a.sort()

for i in range(m):
  num = int(input())
  index = n

  start, end = 0, n-1
  while start <= end:
    mid = (start+end) // 2

    if a[mid] < num:
      start = mid + 1
    elif a[mid] == num:
      index = min(index, mid)
      end = mid - 1
    else:
      end = mid - 1

  print(-1 if index >= n else index)