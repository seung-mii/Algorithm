n = int(input())
drinks = list(map(int, input().split()))
drinks.sort()

total = drinks[n-1]
for i in range(n-1):
  total += drinks[i]/2

print(total)