import sys
input = sys.stdin.readline

n = int(input())
length = sorted([int(input()) for _ in range(n)], reverse=True)
result = -1

for i in range(n-2):
  if length[i] < length[i+1] + length[i+2]:
    result = length[i] + length[i+1] + length[i+2]
    break
 
print(result)