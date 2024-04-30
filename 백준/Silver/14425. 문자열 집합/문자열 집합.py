N,M = map(int, input().split())
result = 0

dictN = {}
for i in range(N):
  dictN[input()] = 0

for j in range(M):
  temp = input()
  if temp in dictN:
    result += 1

print(result)