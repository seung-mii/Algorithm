x,y = map(int, input().split())
z = int(y * 100 / x)
flag = 0

start, end = 1, x
while start <= end:
  mid = (start+end) // 2

  if int((y+mid) * 100 / (x+mid)) > z:
    flag = 1
    end = mid - 1
  else:
    start = mid + 1

if flag == 0:
	print(-1)
else:
  print(start)