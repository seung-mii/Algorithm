n, k = map(int, input().split())
ary = list(map(str, input()))
start = 0
end = 0

for i in range(len(ary)):
  if ary[i] == 'H': 
    if i < k:
      end = i+k+1
    elif n - k <= i:
      start = i-k
      end = n
    else:
      start = i-k
      end = i+k+1

    if start < 0:
      start = 0
    if end > n:
      end = n
      
    for j in range(start, end):
      if ary[j] == 'P':
        ary[i] = ''
        ary[j] = ''
        break
  
print(int(ary.count('') / 2))
