import sys
input = sys.stdin.readline

n, m = map(int, input().split())
point = sorted(list(map(int, input().split())))

def bs(ary, l, switch):
  start, end = 0, n-1
  i = -1

  while start <= end:
    mid = (start + end) // 2

    if ary[mid] <= l:
        i = (mid - 1 if switch == 1 and ary[mid] == l else mid)
        start = mid + 1
    else:
        end = mid - 1

  return i

for i in range(m):
  l1, l2 = map(int, input().split())
  i1, i2 = 0, 0
  i1 = bs(point, l1, 1)
  i2 = bs(point, l2, 2)
  print(i2 - i1)
