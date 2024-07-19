n = int(input())
data = list(map(int, input().split()))
 
height = data[0]
kill = []
count = 0
 
for i in range(1, n):
  if data[i] < height:
    count += 1
  else:
    height = data[i]
    kill.append(count)
    count = 0
  
kill.append(count)
print(max(kill))