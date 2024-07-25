for _ in range(int(input())):
  n,m = map(int, input().split())
  a = sorted(list(map(int, input().split())))
  b = sorted(list(map(int, input().split())))
  cnt = 0

  for i in range(n):
    start, end = 0, m-1

    while start <= end:
      mid = (start + end) // 2

      if b[mid] < a[i]:
        start = mid + 1
      else:
        end = mid - 1
    
    cnt += end + 1

  print(cnt)