t = int(input())

for i in range(t):
  n = int(input())
  start = list(map(str, input()))
  target = list(map(str, input()))
  save = []

  for j in range(n):
    if start[j] != target[j]:
      save.append(start[j])

  if save.count("B") >= save.count("W"):
    print(save.count("B"))
  elif save.count("B") < save.count("W"):
    print(save.count("W"))
  else:
    print(0)