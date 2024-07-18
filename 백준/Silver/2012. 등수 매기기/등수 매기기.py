n = int(input())
ary = []
dis = 0

for i in range(n):
  ary.append(int(input()))

ary.sort()

for i in range(n):
  if ary[i] != i+1:
    dis += abs(ary[i] - (i+1))

print(dis)