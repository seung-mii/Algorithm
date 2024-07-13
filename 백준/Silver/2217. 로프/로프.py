N = int(input())
m = []
result = 0

for i in range(N):
  m.append(int(input()))

m.sort(reverse=True)
result = []

for j in range(N):
  result.append(m[j]*(j+1))

print(max(result))