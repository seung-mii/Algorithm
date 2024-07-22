import sys
input = sys.stdin.readline

n,m = map(int, input().split())
cus = sorted([int(input()) for _ in range(m)], reverse=True)

price = 0
revenue = 0
for i in range(min(n, m)):
  if revenue <= cus[i] * (i+1):
    price = cus[i]
    revenue = cus[i] * (i+1)
  
print(price,revenue)
