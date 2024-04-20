sum = 0
scoresum = 0

for i in range(20):
  a,b,c = input().split()
  if c== 'A+':
    sum += (float(b)*4.5)
    scoresum += float(b)
  elif c== 'A0':
    sum += (float(b)*4.0)
    scoresum += float(b)
  elif c== 'B+':
    sum += (float(b)*3.5)
    scoresum += float(b)
  elif c== 'B0':
    sum += (float(b)*3.0)
    scoresum += float(b)
  elif c== 'C+':
    sum += (float(b)*2.5)
    scoresum += float(b)
  elif c== 'C0':
    sum += (float(b)*2.0)
    scoresum += float(b)
  elif c== 'D+':
    sum += (float(b)*1.5)
    scoresum += float(b)
  elif c== 'D0':
    sum += (float(b)*1.0)
    scoresum += float(b)
  elif c== 'F':
    sum += (float(b)*0.0)
    scoresum += float(b)
  else :
    continue

print(format(sum / scoresum, '.6f'))