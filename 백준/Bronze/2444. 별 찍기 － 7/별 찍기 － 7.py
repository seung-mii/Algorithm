n = int(input())
star = 1
empty = n-1

for i in range(n*2-1):
  if i < n-1:
    for j in range(empty):
      print(' ', end='')
    empty -= 1

    for k in range(star):
      print('*', end='')
    star += 2
    print()
  
  else:
    for j in range(empty):
      print(' ', end='')
    empty += 1
    
    for k in range(star):
      print('*', end='')
    star -= 2
    print()
