n = int(input())
price = 0
milk = []

for i in range(n):
  milk.append(int(input()))

milk.sort(reverse=True)

for i in range(0, n):
  if (i+1) % 3 != 0:
    price += milk[i]

print(price)