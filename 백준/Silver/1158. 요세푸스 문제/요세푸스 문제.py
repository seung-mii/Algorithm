from collections import deque

n, k = map(int, input().split())
num = 0
q1 = deque([])
q2 = deque([])

for i in range(1, n+1):
  q1.append(i)

while len(q1) != 0:
  value = q1.popleft()
  num += 1

  if num % k == 0: 
    q2.append(value)
  else:
    q1.append(value)

print("<", end="")
while len(q2) != 1:
  print(q2.popleft(), end=', ')
print(str(q2.popleft()) + ">")