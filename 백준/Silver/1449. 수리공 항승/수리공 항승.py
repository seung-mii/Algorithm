n, m = map(int, input().split())
position = list(map(int, input().split()))
position.sort()

start = position[0]
count = 1

for i in position[1:]:
  if (i + 0.5) - (start - 0.5) <= m:
    continue
  else:
    start = i
    count += 1

print(count)