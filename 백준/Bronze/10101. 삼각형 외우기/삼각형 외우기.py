arr = []

for i in range(3):
  arr.append(int(input()))

cnt = arr.count(60)

if cnt == 3:
  print('Equilateral')
elif sum(arr) == 180 and len(arr) != len(set(arr)): # 세 각의 합이 180이고 같은 각이 있는 경우
  print('Isosceles')
elif sum(arr) == 180 and len(arr) == len(set(arr)): # 세 각의 합이 180이고 같은 각이 없는 경우
  print('Scalene')
else:
  print('Error')
