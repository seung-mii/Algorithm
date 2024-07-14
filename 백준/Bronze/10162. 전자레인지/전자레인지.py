t = int(input())
num = [0, 0, 0]
time = [300, 60, 10]

for i in range(3):
  if time[i] <= t:
    num[i] += t // time[i]
    t %= time[i]

if t != 0:
  print(-1)
else:
  print(" ".join(map(str, num)))