n = int(input())
shop = list(map(int, input().split()))
drink = 0
milk = 0

for i in range(n):
  if shop[i] == milk:
    drink += 1
    if milk == 0 or milk == 1:
      milk += 1
    else:
      milk = 0

print(drink)