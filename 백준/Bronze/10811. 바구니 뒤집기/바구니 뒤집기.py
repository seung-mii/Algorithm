n,m = list(map(int,input().split()))

d = []
for i in range(n) :
  d.append(i+1)

for a in range(m) :
  i,j = list(map(int,input().split()))
  temp = d[i-1:j]
  temp.reverse()
  d[i-1:j] = temp

for i in range(n) :
  print(d[i], end=' ')