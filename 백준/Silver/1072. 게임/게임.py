x,y = map(int, input().split())
z = int(y * 100 / x)

start, end = 1, x
while start <= end:
  mid = (start+end) // 2

  if int((y+mid) * 100 / (x+mid)) > z:
    end = mid - 1
  else:
    start = mid + 1

if start > x:
	print(-1)
else:
  print(start)