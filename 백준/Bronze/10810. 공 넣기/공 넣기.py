n,m = list(map(int,input().split()))

d = []
for i in range(n) :
  d.append(0)

for a in range(m) :
  i,j,k = list(map(int,input().split()))
  bet = j-i+1
  for b in range(bet) :
    if(d[i-1] != 0) :
      d[i-1] = 0
    d[i-1] = k
    i += 1

for i in range(n) :
  print(d[i], end=' ')