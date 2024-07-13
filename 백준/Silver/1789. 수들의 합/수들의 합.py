s = int(input())
n = 0

for i in range(1, s + 1):
  if s < i:
    break
  else:
    s -= i 
    n += 1

print(n)