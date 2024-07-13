s = int(input())
start = 1
n = 0

while True:
  if s < start:
    break
  else:
    s -= start 
    start += 1
    n += 1

print(n)