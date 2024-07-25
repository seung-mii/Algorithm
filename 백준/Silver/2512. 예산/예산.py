n = int(input())
req = sorted(list(map(int, input().split())))
m = int(input())

if (sum(req) <= m):
  print(max(req))
else:
  start, end = 1, max(req)
  while start <= end:
    mid = (start+end) // 2
    use = 0

    for i in range(n):
      if mid >= req[i]:
        use += req[i]
      else: 
        use += mid
    
    if use > m:
      end = mid - 1
    else:
      start = mid + 1

  print(end)