from collections import Counter

n, m = map(int, input().split())
hamming = 0
ary = []
char_ary = [[] for _ in range(m)] 

for i in range(n):
  ary.append(list(map(str, input())))

for i in range(m):
  for j in range(n):
    char_ary[i].append(ary[j][i])

  char_ary[i].sort()
  c = Counter(char_ary[i]).most_common(1)[0][0]
  print(c, end='')

  for j in range(n):
    if char_ary[i][j] != c:
      hamming += 1

print('\n' + str(hamming))
