n = int(input())
ary = list(map(int, input().split())) 
current_sum = -1000
max_sum = -1000

for i in range(n):
  current_sum = max(ary[i], current_sum + ary[i])
  max_sum = max(max_sum, current_sum)

print(max_sum)