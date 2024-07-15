n = int(input())
s = input()

if 'L' in s:
  people = (n + 1) - int(s.count('L') / 2)
else:
  people = n 

print(people)