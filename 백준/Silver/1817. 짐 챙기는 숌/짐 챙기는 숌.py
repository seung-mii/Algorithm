n,m = map(int,input().split())
box = 0

if n == 0: 
  print(box)
else: 
  books = list(map(int,input().split()))
  weight = 0
  box = 1 
  for book in books:   
    if book + weight <= m: 
      weight += book
    else: 
      weight = book 
      box += 1
  print(box)