while True:
  n = int(input())
  arr = []
  sum = 0

  if n == -1:
    break

  for i in range(1, n):
    if n % i == 0:
      sum += i
      arr.append(i)

  if sum == n:
    print(n, '= ', end='')
    for j in range(len(arr)):
      if j == len(arr) - 1:
        print(arr[j])
      else:
        print(arr[j],'+ ', end='')
  else:
    print(n, 'is NOT perfect.')
