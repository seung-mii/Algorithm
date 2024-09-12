n = int(input()) 
grape = [0] * (n+1)

for i in range(1, n+1):
  grape[i] = int(input()) 

dp = [0, grape[1]]

if n > 1:
  dp.append(grape[1] + grape[2])

for i in range(3, n+1): 
  dp.append(max(dp[i-1], grape[i] + grape[i-1] + dp[i-3], grape[i] + dp[i-2]))

print(max(dp))