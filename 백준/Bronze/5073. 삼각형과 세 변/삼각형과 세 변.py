arr = []

while True:
  a,b,c = map(int, input().split())

  if a == 0:
    break

  if sum((a, b, c)) - max((a, b, c)) <= max((a, b, c)):
    print('Invalid')
  elif a == b and b == c:
    print('Equilateral')
  elif a != b and b != c and a != c:
    print('Scalene')
  else:
    print('Isosceles')
