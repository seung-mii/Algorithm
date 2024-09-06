t = int(input())

for _ in range(t):
  n = int(input())
  num = [1, 0]

  for i in range(n):
    num[0], num[1] = num[1], num[0] + num[1] 

  print(num[0], num[1])