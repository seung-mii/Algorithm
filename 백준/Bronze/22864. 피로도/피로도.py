a,b,c,m = map(int, input().split())
fat = 0
finish = 0

for i in range(24):
  if fat < 0:
    fat = 0

  if (fat + a) <= m: # 번아웃 오기 전
    fat += a
    finish += b
  else:
    fat -= c

print(finish)