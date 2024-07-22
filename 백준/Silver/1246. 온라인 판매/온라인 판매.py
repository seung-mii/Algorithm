import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
P = sorted((int(input()) for _ in range(M)), reverse = True)

max_profit = 0
price = 0

for i in range(min(M, N)):
    profit = (i+1) * P[i]
    if max_profit <= profit:
        price = P[i]
        max_profit = profit
        
print(price, max_profit)