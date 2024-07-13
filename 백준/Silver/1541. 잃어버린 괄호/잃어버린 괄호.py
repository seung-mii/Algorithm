str1 = input().split('-')

for i in range(len(str1)):
  if '+' in str1[i]:
    str1[i] = sum(map(int,(str1[i].split('+'))))
  else:
    str1[i] = int(str1[i])

print(str1[0]-sum(str1[1:]))