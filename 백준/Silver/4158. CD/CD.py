import sys
input = sys.stdin.readline

while True:
  n, m = map(int, input().split())
  n_number = {int(input()) for _ in range(n)}
  m_number = {int(input()) for _ in range(m)}

  if n == 0 and m == 0:
    break
  
  print(len(n_number & m_number)) # 교집합