N,K = map(int, input().split())
dictN = {}
num = 0

for i in range(N):
  dictN[i] = int(input())

for j in range(N-1, -1, -1):
  if dictN[j] > K :
    continue
  elif dictN[j] <= K :
    temp = K
    num += (temp // dictN[j]) # num += K의 몫
    K %= dictN[j]

print(num)