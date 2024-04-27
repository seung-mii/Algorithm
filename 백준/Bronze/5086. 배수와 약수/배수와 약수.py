while True:
  a,b = input().split()

  if int(a) == 0 and int(b) == 0:
    break

  if int(b) % int(a) == 0 and int(b) // int(a) > 0:
    print('factor')
  elif int(a) % int(b) == 0 and int(a) // int(b) > 0:
    print('multiple')
  else :
    print('neither')