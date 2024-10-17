from collections import deque

for _ in range(int(input())):
  n, m = map(int, input().split()) 
  ary = list(map(int, input().split())) 
  order = 0 

  q = deque([])
  for i in range(n):
    q.append((ary[i], i))

  while q:
    current = q.popleft()
   
    if len(q) > 0 and current[0] < max(q)[0]:
      q.append(current) 
    else:
      order += 1 
      if current[1] == m: 
        print(order)
        break