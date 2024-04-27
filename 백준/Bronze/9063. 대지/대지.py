n = int(input())
minX,minY,maxX,maxY = 0, 0, 0, 0

if n == 1:
  print(0)
else:
  for i in range(n):
    x,y = map(int, input().split())

    if i == 0:
      minX,minY,maxX,maxY = x, y, x, y
    else: 
      if x < minX:
        minX = x
      if x > maxX:
        maxX = x
      if y < minY:
        minY = y
      if y > maxY:
        maxY = y
    
  print((maxX - minX)*(maxY - minY))
