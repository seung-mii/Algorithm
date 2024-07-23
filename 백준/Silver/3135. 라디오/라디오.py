a,b = map(int, input().split())
n = int(input())
freq = []

freq.append(abs(a-b))
for i in range(n):
  freq.append(abs(int(input())-b)+1)

print(min(freq))