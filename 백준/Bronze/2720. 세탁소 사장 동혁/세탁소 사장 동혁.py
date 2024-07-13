t = int(input())
money = [25, 10, 5, 1]

for i in range(t):
  c = int(input())
  for j in range(4):
    print(c // money[j], end=" ")
    c %= money[j]
  print()