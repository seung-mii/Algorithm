import sys
input = sys.stdin.readline

n = int(input())
line = []

for i in range(n):
  line.append(list(map(int, input().split())))
line.sort()

time = line[0][0] + line[0][1]
for i in range(1, n):
  if time <= line[i][0]:
    time += (line[i][0] - time) + line[i][1]
  else:
    time += line[i][1]

print(time)
