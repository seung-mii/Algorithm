import sys
input = sys.stdin.readline

n = int(input())

start, end = 1, n
q = n
while start <= end:
  mid = (start+end) // 2

  if (mid*mid) >= n:
    q = min(q, mid)
    end = mid - 1
  else:
    start = mid + 1

print(q)