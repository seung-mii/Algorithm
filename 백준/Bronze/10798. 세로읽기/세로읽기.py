d = []

for i in range(5):
  d.append([])

for i in range(5) :
  s = input()
  for j in range(len(s)):
    d[i].append(s[j])

for i in range(15) :
  for j in range(5):
    try:
        print(d[j][i], end='')
    except IndexError:
        pass