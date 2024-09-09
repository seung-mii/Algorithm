n = int(input())
ary = [0, 1, 2, 3]

for i in range(4, n+1):
  ary.append(ary[i-1] + ary[i-2])

print(ary[n] % 10007)