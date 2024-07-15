n = int(input())
people = 0
candidate = []

for i in range(n):
  candidate.append(int(input()))

while True:
  best = max(candidate)
  if best != candidate[0]: 
    candidate[candidate.index(best)] -= 1
    people += 1
    candidate[0] += 1
  else:
    if candidate.count(best) != 1:
      people += 1
    break

print(people)