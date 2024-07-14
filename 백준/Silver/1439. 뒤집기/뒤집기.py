s = input()
num = 0

for i in range(len(s)-1):
  if s[i] == s[0] and s[i+1] != s[0]:
    num += 1

print(num)
