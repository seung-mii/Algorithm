import sys
input = sys.stdin.readline

while True:
  n, m = map(int, input().split())
  if n == 0 and m == 0:
    break

  n_number = [int(input()) for _ in range(n)]
  m_number = [int(input()) for _ in range(m)]
  cd = 0

  for i in range(m):
    start, end = 0,  n-1

    while start <= end:
      mid = (start+end) // 2

      if n_number[mid] == m_number[i]:
        cd += 1
        break
      elif n_number[mid] > m_number[i]:
        end = mid - 1
      elif n_number[mid] < m_number[i]:
        start = mid + 1
  print (cd)