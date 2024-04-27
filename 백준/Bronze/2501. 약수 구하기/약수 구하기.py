n,k = map(int, input().split())
m = 0

for i in range(1, n+1):
  if n % i == 0:
    m += 1
  
  if m == k:
    print(i)
    break

  if m != k and i == n:
    print(0)
