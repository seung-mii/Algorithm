case = 1  

while True:
  l, p, v = map(int, input().split())
  day = 0

  if l == 0 and p == 0 and v == 0:
    break
  
  day += (v // p) * l
  v %= p

  if v > l: day += l
  else: day += v

  print('Case ' + str(case) + ':', day)
  case += 1