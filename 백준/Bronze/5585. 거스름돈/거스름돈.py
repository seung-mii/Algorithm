money = 1000 - int(input())

change = [500, 100, 50, 10, 5, 1]
count = 0

for i in range(6):
  count += money // change[i]
  money %= change[i]

print(count)