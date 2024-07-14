n, m = map(int, input().split())
brand = []
money = 0

for i in range(m):
  brand.append(list(map(int, input().split())))
    
brand.sort()
min_value = min(min(subarray) for subarray in brand)

if n >= 6:
  if min_value*6 < brand[0][0]: 
    money += min_value*n
  else:
    money += brand[0][0]*(n//6)
    n %= 6    
    if brand[0][0] < min_value*n:
      money += brand[0][0]
    else:
      money += min_value*n
else:
  money += min_value*n

print(money)