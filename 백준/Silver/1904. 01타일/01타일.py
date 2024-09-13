n = int(input())
dp = [1, 2, 3]

for i in range(3, n+1):
  dp[(i-1) % 3] = (dp[i % 3] + dp[(i+1) % 3]) % 15746

print(dp[(n-1) % 3])