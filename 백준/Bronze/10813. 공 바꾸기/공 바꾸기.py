n,m = list(map(int,input().split()))

d = []
for i in range(n) :
  d.append(i+1)

for a in range(m) :
  i,j = list(map(int,input().split()))
  temp = d[i-1]
  d[i-1] = d[j-1]
  d[j-1] = temp

for i in range(n) :
  print(d[i], end=' ')