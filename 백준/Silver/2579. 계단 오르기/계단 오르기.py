n = int(input())
stair = [0]
for _ in range(1, n+1):
  stair.append(int(input()))

if n == 1:
  print(stair[1])
elif n == 2:
  print(stair[1] + stair[2])
else:
  dp = [0, stair[1], stair[1] + stair[2]]
    
  for i in range(3, n+1):
    dp.append(max(stair[i] + dp[i-2], stair[i] + stair[i-1] + dp[i-3]))
    
  print(dp[n])