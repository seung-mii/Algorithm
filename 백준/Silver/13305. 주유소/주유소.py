N = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
stard = price[0]
for i in range(N-1):
  if price[i] < stard:
    stard = price[i]
  result += stard*length[i]
  
print(result)
