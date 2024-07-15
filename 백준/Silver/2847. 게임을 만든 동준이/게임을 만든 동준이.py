n = int(input())
de = 0
score = []

for i in range(n):
  score.append(int(input()))

for i in range(n-1, 0, -1):
  if score[i-1] - score[i] > 0:
    de += (score[i-1] - score[i] + 1)
    score[i-1] = score[i] - 1
  elif score[i-1] - score[i] == 0:
    de += 1
    score[i-1] = score[i] - 1

print(de)