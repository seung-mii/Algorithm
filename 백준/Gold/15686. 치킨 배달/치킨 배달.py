import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))
result = 999999
house = []     
chickens = []     

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      house.append([i, j])
    elif graph[i][j] == 2:
      chickens.append([i, j])

for chicken in combinations(chickens, m):  
  temp = 0 
  for h in house: 
    chicken_len = 999  
    for j in range(m):
      chicken_len = min(chicken_len, abs(h[0] - chicken[j][0]) + abs(h[1] - chicken[j][1]))
    temp += chicken_len
  result = min(result, temp)

print(result)